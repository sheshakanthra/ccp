# 4. DATA FLOW DIAGRAMS

## 4.1 DFD Level 0 (Context Diagram)
The Civic Issue Management System interacts with citizens, administrators, Supabase storage, and a system scheduler. Citizens submit issues and images, administrators retrieve prioritized issues and update status, Supabase stores image data, and the scheduler triggers automated escalation.

## 4.2 DFD Level 1 (Detailed Diagram)
- **P1**: User Authentication (JWT-based login)
- **P2**: Issue Registration (data validation, image upload, database insertion)
- **P3**: Sequential Risk Escalation Engine (time-based state evaluation and escalation)
- **P4**: Issue Retrieval (priority-based querying)
- **P5**: Issue Resolution (status update and removal from escalation loop)

Data stores include Users, Issues, Escalation Logs, and Supabase Storage. The escalation engine operates independently, implementing finite state transitions based on time thresholds.
