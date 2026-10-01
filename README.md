Library Audit Tool & Management CLI

A professional, database-driven CLI application for auditing, tracking, and managing library inventory, member registrations, and loan operations. 

Originally built using SQLite, this tool has been upgraded to **PostgreSQL** to leverage enterprise-grade relational database management and Role-Based Access Control and Restrictions enforced directly at the database engine level.

---
Key Features

*Database Engine Migration: Upgraded from SQLite (`books.db`) to PostgreSQL (`library`) for improved concurrency, data integrity, and performance.
*Database-Level Authorization: Replaced manual application permission logic with native PostgreSQL roles (`admin`, `Manager`, `user`) managed via pgAdmin/SQL.
*Modular Codebase: Architected with clear separation of concerns between database interaction logic, application controllers, and CLI presentation.

---

## 🛠️ Tech Stack & Dependencies

*Language: Python 3.10+
*Database Engine: PostgreSQL 15+
*Database Driver: `psycopg2`
*Database GUI: pgAdmin 4

---

## System Architecture & Security

This project delegates user authorization directly to PostgreSQL:

1. Role-Based Access Control (RBAC): User privileges are enforced by PostgreSQL roles configured via SQL/pgAdmin rather than hardcoded Python dictionaries.
2. **Graceful Exception Handling**: Unauthorised database operations trigger exceptions, which the application catches and surfaces cleanly to the user.

---

Prerequisites

* Python 3.10 or higher installed.
* PostgreSQL installed and running locally on port `5432`.
* pgAdmin or `psql` shell access.

Repository Setup

```bash
# Clone the repository
git clone [https://github.com/your-username/library-audit-tool.git](https://github.com/your-username/library-audit-tool.git)
cd library-audit-tool

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
