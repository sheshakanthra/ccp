# Backend Design Document

## Overview
This document outlines the backend architecture of the Risk-Aware Civic Issue Management System.
The backend is implemented using FastAPI and follows a layered architecture to ensure modularity,
scalability, and maintainability.

## Architecture Layers
- API Layer (FastAPI): Handles HTTP requests and responses
- Service Layer: Contains business logic such as sequential risk escalation
- Data Access Layer: Manages database interactions using SQLAlchemy ORM
- Background Scheduler: Executes automated escalation checks using APScheduler
- External Storage Layer: Supabase is used for image storage

## Core Components
- Authentication using JWT
- Issue management APIs (create, view, resolve)
- Sequential risk escalation engine
- Priority-based sorting mechanism

## Design Note
This document represents the initial architectural blueprint. The finalized and refined
implementation details are captured in the final project documentation files.
