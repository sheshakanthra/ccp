from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .models import RiskLevel, Status

class UserCreate(BaseModel):
    email: str
    password: str
    full_name: str

class UserRead(BaseModel):
    id: int
    email: str
    full_name: str
    role: str

class IssueCreate(BaseModel):
    title: str
    description: str
    category: str
    risk_level: RiskLevel = RiskLevel.LOW

class IssueRead(BaseModel):
    id: int
    title: str
    description: str
    category: str
    risk_level: RiskLevel
    status: Status
    priority_score: float
    image_url: Optional[str]
    created_at: datetime
    last_escalated_at: datetime
