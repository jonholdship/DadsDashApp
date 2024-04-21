from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class TokenResponse(BaseModel):
    token: str


class UserSettings(BaseModel):
    class Config:
        json_encoders = {
            datetime: lambda v: v.date().isoformat(),
        }

    athlete_id: int
    start_date: datetime
    end_date: Optional[datetime]

    # @field_serializer("start_date")
    # @field_serializer("end_date")
    # def serialize_date(self, dt: datetime, _info):
    #     return dt.date()
