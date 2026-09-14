# Automated Library Audit & Alert System

A robust, object-oriented Python backend tool designed to manage library inventory databases, track stock thresholds, and safely generate low-stock alerts. Built with a focus on production-grade software engineering standards, security, and defensive programming.

## Key Features

- **Repository Pattern Architecture:** Encapsulates raw database operations inside a dedicated `LibraryAudit` class for clean separation of concerns.
- **Custom Exception Hierarchy:** Replaces raw SQLite crashes with domain-specific exceptions (`DatabaseConnectionError`, `AuditExceptionError`) for predictable error handling.
- **SQL Injection Prevention:** Utilizes parameterized queries (`?` placeholders) across all dynamic database interactions.
- **Input Validation:** Enforces type safety and non-negative integer boundaries before executing query operations.
- **Resource Management:** Ensures proper lifecycle management of database connections and cursors to prevent connection leaks.

# Tech Stack

- **Language:** Python 3.x
- **Database:** SQLite3

# Database Schema

The application operates on the `mini_library` table:

| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | INTEGER | Primary Key |
| `title` | TEXT | Book Title |
| `available_copies` | INTEGER | Current stock count |



### Prerequisites
- Python 3.8+ installed on your system.

### Setup & Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/library-audit-tool.git](https://github.com/your-username/library-audit-tool.git)
   cd library-audit-tool
