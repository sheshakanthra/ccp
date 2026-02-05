# 2. NOVELTY AND INNOVATION

## 2.1 Sequential Time-Based Risk Escalation
Unlike traditional civic issue systems that rely on static priorities or cumulative age-based deadlines, this project introduces a sequential state-duration escalation model. Each unresolved issue progresses through predefined risk levels based on the duration spent in its current state:
- Low → Medium after 24 hours
- Medium → High after 12 hours
- High → Critical after 6 hours

Escalation decisions are based on the `last_escalated_at` timestamp, ensuring fair and controlled progression without sudden priority jumps.

## 2.2 Hybrid Risk Assessment Model
The system combines user-defined initial risk classification with automated system-driven escalation. This hybrid approach respects citizen input while preventing neglect. If a user reports an issue as High, the system immediately treats it as urgent and escalates it to Critical if unresolved within 6 hours.

## 2.3 Temporal State Tracking Architecture
The introduction of `last_escalated_at` enables a temporal state machine design. Each escalation resets the state timer, allowing precise tracking of time spent in each risk level and enabling predictable escalation behavior aligned with real-world SLA models.

## 2.4 Audit Trail with State Transition Semantics
All escalation events are logged in the `escalation_logs` table with previous and new risk levels and timestamps. This provides:
- Accountability through complete escalation history
- Analytical insights into systemic delays
- Transparency for both administrators and citizens

## 2.5 Priority-Based Sorting Algorithm
A numerical `priority_score` is calculated using a base weight for each risk level combined with time spent in the current state. This ensures:
- Critical issues are always prioritized
- Older unresolved issues within the same risk tier surface first

## 2.6 Scalability Through Asynchronous Architecture
The use of FastAPI’s asynchronous processing and decoupled image storage enables:
- Non-blocking concurrent uploads
- Independent execution of escalation logic
- Horizontal scalability through stateless authentication

## 2.7 Academic Contribution
This project demonstrates the application of finite state machine principles and time-based workflow automation to civic technology. The sequential escalation model is reusable in domains such as customer support systems, healthcare triage, and incident management platforms.
