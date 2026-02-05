from datetime import datetime, timedelta
from sqlmodel import Session, select
from ..database import engine
from ..models import Issue, Status, RiskLevel

# Configuration for sequential escalation
ESCALATION_RULES = {
    RiskLevel.LOW: {"next": RiskLevel.MEDIUM, "hours": 24, "score": 2.0},
    RiskLevel.MEDIUM: {"next": RiskLevel.HIGH, "hours": 12, "score": 3.0},
    RiskLevel.HIGH: {"next": RiskLevel.CRITICAL, "hours": 6, "score": 5.0},
    RiskLevel.CRITICAL: {"next": None, "hours": 0, "score": 10.0} # Max level
}

RISK_SCORES = {
    RiskLevel.LOW: 1.0,
    RiskLevel.MEDIUM: 2.0,
    RiskLevel.HIGH: 3.0,
    RiskLevel.CRITICAL: 5.0
}

def run_escalation_check():
    """
    Scheduled job to escalate issues based on time in current state.
    Logic:
    - Low -> Medium after 24h from last_escalated_at
    - Medium -> High after 12h from last_escalated_at
    - High -> Critical after 6h from last_escalated_at
    """
    print(f"[{datetime.utcnow()}] Running Escalation Check...")
    with Session(engine) as session:
        # Fetch all OPEN issues that are NOT yet Critical
        statement = select(Issue).where(
            Issue.status == Status.OPEN,
            Issue.risk_level != RiskLevel.CRITICAL
        )
        issues = session.exec(statement).all()
        
        count_escalated = 0
        
        for issue in issues:
            current_rule = ESCALATION_RULES.get(issue.risk_level)
            if not current_rule or not current_rule["next"]:
                continue
                
            time_threshold = timedelta(hours=current_rule["hours"])
            time_in_state = datetime.utcnow() - issue.last_escalated_at
            
            if time_in_state >= time_threshold:
                previous_risk = issue.risk_level
                
                # Escalate
                issue.risk_level = current_rule["next"]
                issue.priority_score = current_rule["score"]
                issue.last_escalated_at = datetime.utcnow()
                
                session.add(issue)
                count_escalated += 1
                
                print(f"Escalated Issue #{issue.id}: {previous_risk} -> {issue.risk_level}")
        
        if count_escalated > 0:
            session.commit()
            print(f"Updated {count_escalated} issues.")
        else:
            print("No issues required escalation.")
