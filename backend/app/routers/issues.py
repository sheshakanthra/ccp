from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select, desc
from typing import List, Optional
from ..database import get_session
from ..models import Issue, Status, RiskLevel, User
from ..schemas import IssueCreate, IssueRead
from datetime import datetime

router = APIRouter(prefix="/issues", tags=["Issues"])

@router.post("/", response_model=IssueRead)
def create_issue(
    issue_data: IssueCreate, 
    session: Session = Depends(get_session)
):
    # Calculate initial score
    initial_score = 1.0
    if issue_data.risk_level == RiskLevel.MEDIUM: initial_score = 2.0
    elif issue_data.risk_level == RiskLevel.HIGH: initial_score = 3.0
    elif issue_data.risk_level == RiskLevel.CRITICAL: initial_score = 5.0

    issue = Issue(
        **issue_data.dict(),
        priority_score=initial_score,
        created_at=datetime.utcnow(),
        last_escalated_at=datetime.utcnow()
    )
    session.add(issue)
    session.commit()
    session.refresh(issue)
    return issue

@router.get("/", response_model=List[IssueRead])
def read_issues(
    status: Optional[Status] = None,
    session: Session = Depends(get_session)
):
    query = select(Issue).order_by(desc(Issue.priority_score))
    if status:
        query = query.where(Issue.status == status)
        
    results = session.exec(query).all()
    return results

@router.patch("/{issue_id}/resolve")
def resolve_issue(issue_id: int, session: Session = Depends(get_session)):
    issue = session.get(Issue, issue_id)
    if not issue:
        raise HTTPException(status_code=404, detail="Issue not found")
        
    issue.status = Status.RESOLVED
    session.add(issue)
    session.commit()
    return {"message": "Issue resolved"}
