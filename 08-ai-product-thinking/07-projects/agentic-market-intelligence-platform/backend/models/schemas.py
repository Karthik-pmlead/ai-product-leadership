from pydantic import BaseModel

from typing import List


class AnalysisRequest(
    BaseModel
):
    query: str


class AnalysisResponse(
    BaseModel
):

    intent: str

    summary: str

    risks: List[str]

    opportunities: List[str]

    recommendations: List[str]

    sources: List[str]

    workflow: List[str]

    trace: list[dict]
