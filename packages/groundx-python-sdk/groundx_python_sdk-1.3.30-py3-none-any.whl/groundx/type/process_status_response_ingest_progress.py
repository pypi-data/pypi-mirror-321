# coding: utf-8

"""
    GroundX APIs

    RAG Made Simple, Secure and Hallucination Free

    The version of the OpenAPI document: 1.3.26
    Contact: support@eyelevel.ai
    Created by: https://www.eyelevel.ai/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from groundx.type.process_status_response_ingest_progress_cancelled import ProcessStatusResponseIngestProgressCancelled
from groundx.type.process_status_response_ingest_progress_complete import ProcessStatusResponseIngestProgressComplete
from groundx.type.process_status_response_ingest_progress_errors import ProcessStatusResponseIngestProgressErrors
from groundx.type.process_status_response_ingest_progress_processing import ProcessStatusResponseIngestProgressProcessing

class RequiredProcessStatusResponseIngestProgress(TypedDict):
    pass

class OptionalProcessStatusResponseIngestProgress(TypedDict, total=False):
    cancelled: ProcessStatusResponseIngestProgressCancelled

    complete: ProcessStatusResponseIngestProgressComplete

    errors: ProcessStatusResponseIngestProgressErrors

    processing: ProcessStatusResponseIngestProgressProcessing

class ProcessStatusResponseIngestProgress(RequiredProcessStatusResponseIngestProgress, OptionalProcessStatusResponseIngestProgress):
    pass
