# 1. METHODOLOGY

## 1.1 Research Design
This project follows an applied research methodology aimed at developing a practical and automated solution for managing civic issues reported by citizens. The system is designed to address real-world urban problems such as electricity failures, water supply disruptions, drainage issues, and road damage. An incremental software development model is adopted, consisting of requirement analysis, system design, implementation, and testing phases. This approach enables iterative refinement and validation of system functionality.

## 1.2 Technology Stack Selection
The technology stack was chosen based on scalability, performance, and relevance to modern web-based systems:

- **Backend Framework**: FastAPI is used due to its asynchronous request handling, high performance, and automatic API documentation through OpenAPI. These features make it suitable for concurrent issue submissions and image uploads.
- **Database Management**: PostgreSQL with SQLAlchemy ORM provides ACID compliance, structured relational modeling, and efficient query execution for managing users, issues, and escalation logs.
- **Storage Solution**: Supabase cloud storage is utilized for storing image evidence uploaded by users. Only the image URLs are stored in the database, reducing storage overhead.
- **Authentication**: JSON Web Tokens (JWT) are implemented to enable stateless authentication and role-based access control for citizens and administrators.
- **Task Scheduling**: APScheduler is used to execute the automated risk escalation engine periodically without introducing complex external task queues, keeping the system university-project friendly.

## 1.3 System Development Process

### Phase 1: Requirements Gathering
- Identified primary stakeholders: citizens (issue reporters) and administrators (issue resolvers)
- Defined core functionalities: issue reporting, image attachment, automatic sequential risk escalation, and priority-based issue sorting
- Established business rules for state-based time thresholds in risk escalation

### Phase 2: Database Design
- Designed a normalized relational schema with three main entities: users, issues, and escalation_logs
- Implemented foreign key constraints and indexing strategies for performance optimization
- Used enumerated types for risk levels and issue status to enforce data consistency
- Added a `last_escalated_at` timestamp field to track time spent in each risk state

### Phase 3: API Development
- Designed RESTful endpoints following OpenAPI standards
- Implemented request validation using Pydantic schemas
- Developed CRUD operations using appropriate HTTP methods

### Phase 4: Business Logic Implementation
- Implemented a sequential risk escalation engine based on state duration
- Developed a priority scoring mechanism combining risk severity and time spent in the current state
- Added audit logging for all risk state transitions

### Phase 5: Testing and Validation
- Unit testing of service-layer functions
- Integration testing of API endpoints
- Time-based testing of sequential escalation using simulated timestamps
- Validation of the `last_escalated_at` update mechanism

## 1.4 Data Flow Management
The system follows a layered architecture:
- **Presentation Layer**: Handles HTTP requests and responses
- **Business Logic Layer**: Processes escalation rules and application logic
- **Data Access Layer**: Manages database transactions via ORM
- **External Services Layer**: Handles image storage through Supabase
