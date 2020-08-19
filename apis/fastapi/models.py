# noinspection PyPackageRequirements
from pydantic import BaseModel


class TextCategorizationInput(BaseModel):

    text: str


class TextCategorizationOutput(BaseModel):

    text: str
    prediction_id: str
    category: int
