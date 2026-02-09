# Seashell API

This API was created as a technical assignment for Kone's Cloud Developer Summer Intern position.
It was designed to catalog seashells. It provides a robust, containerized solution for managing seashell data.

## Getting started

### Prerequisites

Docker and Docker compose installed on your machine.

### Installation & setup

### 1. Clone the repository

```python
git clone https://github.com/JSalevaara/Seashell_API_Task.git
cd Seashell_API_Task
```

### (Optional when running with Docker) Configure environment variables

Create a file called .env to the root of the project.

```bash
touch .env
```

Paste the following content to the .env file or choose your own. \

```
DB_USER=testuser
DB_PASSWORD=testpassword
DB_NAME=seashelldb
DATABASE_URL=postgresql://${DB_USER:-user}:${DB_PASSWORD:-password}@localhost:5432/${DB_NAME:-seashell_db}
```

_You can choose DB_USER, DB_PASSWORD, DB_NAME freely._ \
_Just make sure the file contains DB_USER, DB_PASSWORD, DB_NAME, DATABASE_URL when running the API without Docker._

### 2. Start the environment

```bash
docker-compose up --build
```

_The API will be available at `localhost:8000` and the database will persist data using Docker volumes._

## API Documentation

FastAPI automatically generates interactive documentation. Once the server is running, you can explore and test the endpoints directly:

**Swagger UI:** `http://localhost:8000/docs` \
**ReDoc:** `http://localhost:8000/redoc`

#### Endpoints

| Method     | Endpoint        | Description                                    |
| :--------- | :-------------- | :--------------------------------------------- |
| **GET**    | /seashells      | List all seashelss in the database             |
| **POST**   | /seashells      | Add a new seashell (name and species required) |
| **PUT**    | /seashells/{id} | Update an existing seashell's details by ID.   |
| **DELETE** | /seashells/{id} | Remove a seashell from the treasury.           |

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

## Tech Stack

- **Framework:** FastAPI, for high-performance
- **Database:** Postgresql 13, for reliability
- **ORM:** SQLAlchemy 2.0, for handling SQL data with Python classes
- **Validation:** Pydantic 2.12, for type enforcement and data integrity
- **Containerization:** Docker, for a consistent environment

## Project structure

## Advanced features
