# Risk Escalation Logic

## Escalation Model
The system uses a sequential, state-duration-based risk escalation model.
Escalation decisions are based on the time spent in the current risk state,
tracked using the `last_escalated_at` timestamp.

## Escalation Rules
- Low → Medium after 24 hours
- Medium → High after 12 hours
- High → Critical after 6 hours

## Key Characteristics
- Escalation is sequential (no skipping of risk levels)
- Each escalation resets the state timer
- Only issues with status = 'Open' are eligible
- Resolved issues are excluded from escalation checks

## Data Updates on Escalation
- Update current_risk_level
- Reset last_escalated_at to current timestamp
- Recalculate priority_score
- Insert record into escalation_logs table

## Rationale
This approach ensures fairness, predictability, and alignment with real-world
service-level escalation practices.
