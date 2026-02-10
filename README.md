# Seashell API

This API was created as a technical assignment for Kone's Cloud Developer Summer Intern position.
It was designed to catalog seashells. It provides a robust, containerized solution for managing seashell data.

## Getting started

### Prerequisites

- For Docker: Docker and Docker compose installed.
- For Local: Python 3.12+ and a running PostgreSQL instance.

## Installation and Setup with Docker (Recommended)

This is the simplest and easiest way to use this API since it handles database and environment setup automatically.

### 1. Clone the repository:

```bash
git clone https://github.com/JSalevaara/Seashell_API_Task.git
cd Seashell_API_Task
```

### 2. Start the environment:

```bash
docker-compose up --build
```

_The API will be available at `localhost:8000` and the database will persist data using Docker volumes._

## Installation and Setup locally

Use this setup if you want to run the application directly on your host machine.

### 1. Clone the repository:

```bash
git clone https://github.com/JSalevaara/Seashell_API_Task.git
cd Seashell_API_Task
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the environment

Create a .env file in the project root and provide your local PostgreSQL connection details.

```plaintext
DATABASE_URL=postgresql://user:password@localhost:5432/seashell_db
```

_Make sure the .env file contains DATABASE_URL which points to the local PostgreSQL instance._

### 5. Start the API.

```bash
uvicorn app.main:app
```

## API Documentation

FastAPI automatically generates interactive documentation. Once the server is running, you can explore and test the endpoints directly:

**Swagger UI:** `http://localhost:8000/docs` \
**ReDoc:** `http://localhost:8000/redoc`

#### Endpoints

| Method     | Endpoint        | Description                                                                          |
| :--------- | :-------------- | :----------------------------------------------------------------------------------- |
| **GET**    | /seashells      | List all seashells in the database                                                   |
| **POST**   | /seashells      | Add a new seashell (name and species required)                                       |
| **PUT**    | /seashells/{id} | Update an entry by ID. Supports partial updates (only provided fields are modified). |
| **DELETE** | /seashells/{id} | Remove a seashell from the database by ID.                                           |

#### Example: Create a seashell

Request body (POST /seashells)

```json
{
    "name": "Giant shell",
    "species": "Special Shell",
    "description": "Large unique shell with green lines going through it.",
    "origin": "Indian Ocean",
    "color": "Pink/Green"
}
```

## Features

- CRUD Operations: Full support for creating, reading, updating and deleting seashell entries.
- Data Persistence: Persistent storage using a PostgreSQL database.
- Partial Updates: Supports only modifying provided fields.
- Automatic Documentation: Provides interactive Swagger and ReDoc documentation automatically through FastAPI.

## Tech Stack

- **Framework:** FastAPI, for high-performance
- **Database:** Postgresql 13, for reliability
- **ORM:** SQLAlchemy 2.0, for handling SQL data with Python classes
- **Validation:** Pydantic 2.12, for type enforcement and data integrity
- **Containerization:** Docker, for a consistent environment

## Project structure

```plaintext
.
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```
