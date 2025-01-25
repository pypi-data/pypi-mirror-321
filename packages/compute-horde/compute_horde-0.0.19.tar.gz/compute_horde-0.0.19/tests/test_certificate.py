import asyncio
import os

import pytest
import requests
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey

from compute_horde.certificate import (
    generate_certificate,
    generate_certificate_at,
    save_public_key,
    start_nginx,
    write_certificate,
)

NGINX_PORT = 8443
NGINX_URI = f"https://localhost:{NGINX_PORT}"

NGINX_CONF = """
http {
    server {
        listen 443 ssl;
        server_name example.com;

        ssl_certificate /etc/nginx/ssl/certificate.pem;
        ssl_certificate_key /etc/nginx/ssl/private_key.pem;

        ssl_client_certificate /etc/nginx/ssl/client.crt;
        ssl_verify_client on;

        location / {
            if ($ssl_client_verify != SUCCESS) { return 403; }
            return 200 'Hello World!';
            add_header Content-Type text/plain;
        }
    }
    
    server {
        listen 80;
        server_name localhost;

        # for checking if nginx is running
        location /ok { return 200; }
    }
}

events {
    worker_connections 1024;
}
"""


def test_generate_ca_and_server_certs(tmp_path):
    generate_certificate_at(tmp_path, "blabla")
    tmp_path = tmp_path / "ssl"

    assert set(os.listdir(tmp_path)) == {"certificate.pem", "private_key.pem"}

    # check the cert is valid
    x509.load_pem_x509_certificate((tmp_path / "certificate.pem").read_bytes())

    # check the public key is valid
    key = serialization.load_pem_private_key((tmp_path / "private_key.pem").read_bytes(), None)
    assert isinstance(key, RSAPrivateKey)


async def start_nginx_with_certificates(
    nginx_conf: str,
    public_key: str,
    port: int,
    container_name: str,
) -> tuple[str, str]:
    tmp_path, _, cert = generate_certificate_at()
    save_public_key(public_key, tmp_path)

    job_network = f"{container_name}_network"
    process = await asyncio.create_subprocess_exec(
        "docker", "network", "create", "--internal", job_network
    )
    await process.wait()

    await start_nginx(
        nginx_conf, port, tmp_path, job_network=job_network, container_name=container_name
    )
    return cert


async def cleanup_docker(container_name):
    process = await asyncio.create_subprocess_exec(
        "docker", "network", "rm", f"{container_name}_network"
    )
    await process.wait()
    process = await asyncio.create_subprocess_exec("docker", "kill", container_name)
    await process.wait()


@pytest.mark.asyncio
async def test_certificates_with_nginx__success(tmp_path, container_name):
    _, public_key, cert = generate_certificate_at(tmp_path)
    nginx_cert_path, _ = await start_nginx_with_certificates(
        NGINX_CONF, public_key, NGINX_PORT, container_name
    )

    resp = requests.get(NGINX_URI, verify=nginx_cert_path, cert=cert)
    assert resp.status_code == 200
    assert resp.text.strip() == "Hello World!"

    await cleanup_docker(container_name)


@pytest.mark.asyncio
async def test_certificates_with_nginx__no_cert(tmp_path, container_name):
    _, public_key, _ = generate_certificate_at(tmp_path)
    nginx_cert_path, _ = await start_nginx_with_certificates(
        NGINX_CONF, public_key, NGINX_PORT, container_name
    )

    resp = requests.get(NGINX_URI, verify=nginx_cert_path)

    # 400 no cert, 403 wrong cert
    assert resp.status_code != 200

    await cleanup_docker(container_name)


@pytest.mark.asyncio
async def test_certificates_with_nginx__fail(tmp_path, container_name):
    _, public_key, _ = generate_certificate_at(tmp_path)
    _ = await start_nginx_with_certificates(NGINX_CONF, public_key, NGINX_PORT, container_name)

    cert_path = tmp_path / "wrong_certificate.pem"
    certificate, _ = generate_certificate("127.0.0.1")
    write_certificate(certificate, cert_path)

    with pytest.raises(requests.exceptions.SSLError):
        requests.get(NGINX_URI, verify=str(cert_path))

    await cleanup_docker(container_name)
