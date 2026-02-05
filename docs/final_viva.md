# 5. VIVA VOCE QUESTIONS AND ANSWERS

Q1. Why did you choose FastAPI?
FastAPI provides asynchronous request handling, high performance, and automatic API documentation, making it ideal for scalable systems handling concurrent uploads and background tasks.

Q2. Explain the sequential escalation algorithm.
The algorithm escalates issues based on time spent in the current risk state using `last_escalated_at`. Each escalation resets the timer, ensuring controlled and fair progression.

Q3. How does the system ensure fairness?
By enforcing minimum time thresholds in each risk state, issues cannot skip levels or escalate unfairly due to initial classification.

Q4. What is the role of escalation logs?
They provide auditability, enable analytics, and ensure transparency by recording every risk transition.

Q5. Why maintain both risk level and priority score?
Risk level provides semantic clarity, while priority score enables precise ordering within the same risk tier.

Q6. What security measures are implemented?
Password hashing, JWT-based authentication, role-based access control, ORM-based query protection, and input validation.

Q7. How can the system scale?
Through async processing, indexed queries, batch escalation updates, and decoupled storage, with future scope for distributed task queues.
