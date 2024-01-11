from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary
from typing import Union, List

async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )
    await summary.save()
    return summary.id

async def getSummary(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary
    return None

async def getAllSummaries() -> List:
    summaries = await TextSummary.all().values()
    return summaries
