from datetime import datetime
from typing import Optional
from enum import Enum
from sqlmodel import SQLModel, Field, Relationship

class RiskLevel(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class Status(str, Enum):
    OPEN = "Open"
    RESOLVED = "Resolved"

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    password_hash: str
    full_name: str
    role: str = "citizen"  # 'citizen' or 'admin'
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Issue(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    category: str
    image_url: Optional[str] = None
    
    # Priority & State
    status: Status = Field(default=Status.OPEN)
    risk_level: RiskLevel = Field(default=RiskLevel.LOW)
    priority_score: float = Field(default=1.0)
    
    # Timestamps for Escalation
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_escalated_at: datetime = Field(default_factory=datetime.utcnow)  # Key for sequential logic
    
    reporter_id: Optional[int] = Field(default=None, foreign_key="user.id")
