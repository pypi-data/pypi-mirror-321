from datetime import timedelta
from typing import ClassVar, Self, TypeAlias, assert_never

from django.db import models

from compute_horde.executor_class import DEFAULT_EXECUTOR_CLASS, ExecutorClass
from compute_horde.receipts import ReceiptType
from compute_horde.receipts.schemas import (
    JobAcceptedReceiptPayload,
    JobFinishedReceiptPayload,
    JobStartedReceiptPayload,
    Receipt,
)


class ReceiptNotSigned(Exception):
    pass


class AbstractReceipt(models.Model):
    job_uuid = models.UUIDField()
    validator_hotkey = models.CharField(max_length=256)
    miner_hotkey = models.CharField(max_length=256)
    validator_signature = models.CharField(max_length=256)
    miner_signature = models.CharField(max_length=256, null=True, blank=True)
    timestamp = models.DateTimeField()

    # https://github.com/typeddjango/django-stubs/issues/1684#issuecomment-1706446344
    objects: ClassVar[models.Manager[Self]]

    class Meta:
        abstract = True
        constraints = [
            models.UniqueConstraint(fields=["job_uuid"], name="receipts_unique_%(class)s_job_uuid"),
        ]
        indexes = [
            models.Index(fields=["timestamp"], name="%(class)s_ts_idx"),
        ]

    def __str__(self):
        return f"job_uuid: {self.job_uuid}"


class JobStartedReceipt(AbstractReceipt):
    executor_class = models.CharField(max_length=255, default=DEFAULT_EXECUTOR_CLASS)
    max_timeout = models.IntegerField()
    is_organic = models.BooleanField()
    ttl = models.IntegerField()

    def to_receipt(self) -> Receipt:
        if self.miner_signature is None:
            raise ReceiptNotSigned("Miner signature is required")

        return Receipt(
            payload=JobStartedReceiptPayload(
                job_uuid=str(self.job_uuid),
                miner_hotkey=self.miner_hotkey,
                validator_hotkey=self.validator_hotkey,
                timestamp=self.timestamp,
                executor_class=ExecutorClass(self.executor_class),
                max_timeout=self.max_timeout,
                is_organic=self.is_organic,
                ttl=self.ttl,
            ),
            validator_signature=self.validator_signature,
            miner_signature=self.miner_signature,
        )

    @classmethod
    def from_receipt(cls, receipt: Receipt) -> "JobStartedReceipt":
        if not isinstance(receipt.payload, JobStartedReceiptPayload):
            raise ValueError(
                f"Incompatible receipt payload type. "
                f"Got: {type(receipt.payload).__name__} "
                f"Expected: {JobStartedReceiptPayload.__name__}"
            )

        return JobStartedReceipt(
            job_uuid=receipt.payload.job_uuid,
            miner_hotkey=receipt.payload.miner_hotkey,
            validator_hotkey=receipt.payload.validator_hotkey,
            miner_signature=receipt.miner_signature,
            validator_signature=receipt.validator_signature,
            timestamp=receipt.payload.timestamp,
            executor_class=receipt.payload.executor_class,
            max_timeout=receipt.payload.max_timeout,
            is_organic=receipt.payload.is_organic,
            ttl=receipt.payload.ttl,
        )


class JobAcceptedReceipt(AbstractReceipt):
    time_accepted = models.DateTimeField()
    ttl = models.IntegerField()

    def to_receipt(self) -> Receipt:
        if self.miner_signature is None:
            raise ReceiptNotSigned("Miner signature is required")

        return Receipt(
            payload=JobAcceptedReceiptPayload(
                job_uuid=str(self.job_uuid),
                miner_hotkey=self.miner_hotkey,
                validator_hotkey=self.validator_hotkey,
                timestamp=self.timestamp,
                time_accepted=self.time_accepted,
                ttl=self.ttl,
            ),
            validator_signature=self.validator_signature,
            miner_signature=self.miner_signature,
        )

    @classmethod
    def from_receipt(cls, receipt: Receipt) -> "JobAcceptedReceipt":
        if not isinstance(receipt.payload, JobAcceptedReceiptPayload):
            raise ValueError(
                f"Incompatible receipt payload type. "
                f"Got: {type(receipt.payload).__name__} "
                f"Expected: {JobAcceptedReceiptPayload.__name__}"
            )

        return JobAcceptedReceipt(
            job_uuid=receipt.payload.job_uuid,
            miner_hotkey=receipt.payload.miner_hotkey,
            validator_hotkey=receipt.payload.validator_hotkey,
            miner_signature=receipt.miner_signature,
            validator_signature=receipt.validator_signature,
            timestamp=receipt.payload.timestamp,
            time_accepted=receipt.payload.time_accepted,
            ttl=receipt.payload.ttl,
        )


class JobFinishedReceipt(AbstractReceipt):
    time_started = models.DateTimeField()
    time_took_us = models.BigIntegerField()
    score_str = models.CharField(max_length=256)

    def time_took(self):
        return timedelta(microseconds=self.time_took_us)

    def score(self):
        return float(self.score_str)

    def to_receipt(self) -> Receipt:
        if self.miner_signature is None:
            raise ReceiptNotSigned("Miner signature is required")

        return Receipt(
            payload=JobFinishedReceiptPayload(
                job_uuid=str(self.job_uuid),
                miner_hotkey=self.miner_hotkey,
                validator_hotkey=self.validator_hotkey,
                timestamp=self.timestamp,
                time_started=self.time_started,
                time_took_us=self.time_took_us,
                score_str=self.score_str,
            ),
            validator_signature=self.validator_signature,
            miner_signature=self.miner_signature,
        )

    @classmethod
    def from_receipt(cls, receipt: Receipt) -> "JobFinishedReceipt":
        if not isinstance(receipt.payload, JobFinishedReceiptPayload):
            raise ValueError(
                f"Incompatible receipt payload type. "
                f"Got: {receipt.payload.__class__.__name__} "
                f"Expected: {JobFinishedReceiptPayload.__name__}"
            )

        return JobFinishedReceipt(
            job_uuid=receipt.payload.job_uuid,
            miner_hotkey=receipt.payload.miner_hotkey,
            validator_hotkey=receipt.payload.validator_hotkey,
            miner_signature=receipt.miner_signature,
            validator_signature=receipt.validator_signature,
            timestamp=receipt.payload.timestamp,
            time_started=receipt.payload.time_started,
            time_took_us=receipt.payload.time_took_us,
            score_str=receipt.payload.score_str,
        )


ReceiptModel: TypeAlias = JobAcceptedReceipt | JobStartedReceipt | JobFinishedReceipt


def receipt_to_django_model(receipt: Receipt) -> ReceiptModel:
    match receipt.payload.receipt_type:
        case ReceiptType.JobAcceptedReceipt:
            return JobAcceptedReceipt.from_receipt(receipt)
        case ReceiptType.JobStartedReceipt:
            return JobStartedReceipt.from_receipt(receipt)
        case ReceiptType.JobFinishedReceipt:
            return JobFinishedReceipt.from_receipt(receipt)
        case _:
            assert_never(receipt.payload.receipt_type)
