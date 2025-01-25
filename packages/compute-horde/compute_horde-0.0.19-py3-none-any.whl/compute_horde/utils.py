import datetime
from typing import Any

import bittensor
import pydantic
from substrateinterface.exceptions import SubstrateRequestException

BAC_VALIDATOR_SS58_ADDRESS = "5HBVrFGy6oYhhh71m9fFGYD7zbKyAeHnWN8i8s9fJTBMCtEE"
MIN_STAKE = 1000
VALIDATORS_LIMIT = 24


class MachineSpecs(pydantic.BaseModel):
    specs: dict[Any, Any]

    def __str__(self) -> str:
        return str(self.specs)


class ValidatorListError(Exception):
    def __init__(self, reason: Exception):
        self.reason = reason


def get_validators(
    netuid=12, network="finney", block: int | None = None
) -> list[bittensor.NeuronInfo]:
    """
    Validators are top 24 neurons in terms of stake, only taking into account those that have at least 1000
    and forcibly including BAC_VALIDATOR_SS58_ADDRESS.
    The result is sorted.
    """
    try:
        subtensor = bittensor.subtensor(network=network)
    except Exception as ex:
        raise ValidatorListError(ex) from ex

    try:
        metagraph = subtensor.metagraph(netuid, block=block)
    except SubstrateRequestException as ex:
        raise ValidatorListError(ex) from ex

    neurons = [
        n
        for n in metagraph.neurons
        if (n.hotkey == BAC_VALIDATOR_SS58_ADDRESS or n.stake.tao >= MIN_STAKE)
    ]
    neurons = sorted(
        neurons, key=lambda n: (n.hotkey == BAC_VALIDATOR_SS58_ADDRESS, n.stake), reverse=True
    )
    return neurons[:VALIDATORS_LIMIT]


def json_dumps_default(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()

    raise TypeError


class Timer:
    def __init__(self, timeout=None):
        self.start_time = datetime.datetime.now()
        self.timeout = timeout

    def passed_time(self):
        return (datetime.datetime.now() - self.start_time).total_seconds()

    def time_left(self):
        if self.timeout is None:
            raise ValueError("timeout was not specified")
        return self.timeout - self.passed_time()


def sign_blob(kp: bittensor.Keypair, blob: str):
    """
    Signs a string blob with a bittensor keypair and returns the signature
    """
    return f"0x{kp.sign(blob).hex()}"
