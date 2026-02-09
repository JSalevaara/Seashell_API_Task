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

### 2. Configure environment variables (optional when running with docker)

```
touch .env
```

Paste the following content to the .env file.
_You can choose DB_USER, DB_PASSWORD, DB_NAME freely_

```
DB_USER=testuser
DB_PASSWORD=testpassword
DB_NAME=seashelldbtest
DATABASE_URL=postgresql://${DB_USER:-user}:${DB_PASSWORD:-password}@localhost:5432/${DB_NAME:-seashell_db}
```

-
