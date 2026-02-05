# 3. SYSTEM WORKFLOW

## 3.1 User Registration and Authentication
Users register with email, password, full name, and role. Passwords are hashed using bcrypt before storage. During login, credentials are verified and a JWT token containing user identity and role is issued.

## 3.2 Issue Reporting (Citizen Flow)
Authenticated citizens submit issues by providing a title, description, category, initial risk level, and an image. The image is uploaded to Supabase, and the issue is stored in the database with status set to Open and `last_escalated_at` initialized to the creation time.

## 3.3 Automatic Sequential Risk Escalation
A background scheduler runs periodically to evaluate unresolved issues. For each open issue, the system calculates time spent in the current risk state using `last_escalated_at`. If thresholds are exceeded, the issue is escalated to the next risk level, the timestamp is reset, and the escalation event is logged.

## 3.4 Admin Dashboard View
Administrators retrieve open issues sorted by priority score. The dashboard displays risk level, time spent in the current state, image evidence, and reporter details, ensuring critical issues appear at the top.

## 3.5 Issue Resolution (Admin Flow)
Administrators mark issues as resolved. Once resolved, the issue is excluded from future escalation checks. The final state timestamps are preserved for analytics.
