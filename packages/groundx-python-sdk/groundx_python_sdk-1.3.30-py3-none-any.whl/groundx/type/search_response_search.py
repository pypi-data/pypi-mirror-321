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

from groundx.type.search_result_item import SearchResultItem

class RequiredSearchResponseSearch(TypedDict):
    pass

class OptionalSearchResponseSearch(TypedDict, total=False):
    # Total results
    count: int

    # Search results
    results: typing.List[SearchResultItem]

    # The original search request query
    query: str

    # Confidence score in the search results
    score: typing.Union[int, float]

    # The actual search query, if the search request query was re-written
    searchQuery: str

    # Suggested context for LLM completion
    text: str

    # For paginated results
    nextToken: str

class SearchResponseSearch(RequiredSearchResponseSearch, OptionalSearchResponseSearch):
    pass
