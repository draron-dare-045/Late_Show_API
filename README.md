# Flask Late Show API

A complete REST API for managing a Late Night TV show system built with Flask, PostgreSQL, and JWT authentication.

##  Features

- **MVC Architecture** - Clean separation of concerns
- **PostgreSQL Database** - Robust relational database
- **JWT Authentication** - Secure token-based auth

## Tech Stack

- **Backend**: Flask, SQLAlchemy, Flask-Migrate
- **Database**: PostgreSQL
- **Authentication**: Flask-JWT-Extended
- **Testing**: Postman
- **Version Control**: Git & GitHub

## 📁 Project Structure

```
late-show-api-challenge/
├── server/
│   ├── app.py                 # Main Flask application
│   ├── config.py              # Configuration settings
│   ├── seed.py                # Database seeding script
│   ├── models/
│   │   ├── __init__.py        # Database initialization
│   │   ├── user.py            # User model
│   │   ├── guest.py           # Guest model
│   │   ├── episode.py         # Episode model
│   │   └── appearance.py      # Appearance model
│   └── controllers/
│       ├── __init__.py
│       ├── auth_controller.py     # Authentication routes
│       ├── guest_controller.py    # Guest routes
│       ├── episode_controller.py  # Episode routes
│       └── appearance_controller.py # Appearance routes
├── migrations/                # Database migration files
├── challenge-4-lateshow.postman_collection.json
├── .gitignore
├── Pipfile
└── README.md
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL
- Pipenv (or pip)
- Postman (for testing)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/late-show-api-challenge.git
   cd late-show-api-challenge
   ```

2. **Install dependencies:**
   ```bash
   pipenv install
   pipenv shell
   ```

3. **Set up PostgreSQL:**
   ```sql
   -- Connect to PostgreSQL and create database
   CREATE DATABASE late_show_db;
   ```

4. **Configure environment variables:**
   
   Create a `.env` file in the project root:
   ```env
   SECRET_KEY=your-super-secret-key-here
   JWT_SECRET_KEY=jwt-secret-string-here
   DATABASE_URI=postgresql://username:password@localhost:5432/late_show_db
   ```

5. **Initialize the database:**
   ```bash
   export FLASK_APP=server/app.py
   flask db init
   flask db migrate -m "initial migration"
   flask db upgrade
   ```

6. **Seed the database:**
   ```bash
   python -m server.seed
   ```

7. **Run the application:**
   ```bash
   python -m server.app
   flask run
   ```

The API will be available at `http://localhost:5000`

## Authentication Flow

### 1. Register a New User
```http
POST /register
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
```

**Response:**
```json
{
    "message": "User created successfully",
    "user": {
        "id": 1,
        "username": "your_username"
    }
}
```

### 2. Login to Get JWT Token
```http
POST /login
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
```

**Response:**
```json
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "user": {
        "id": 1,
        "username": "your_username"
    }
}
```

### 3. Use Token in Protected Routes
Add the token to the Authorization header:
```http
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

## API Routes

| Route | Method | Auth Required | Description |
|-------|--------|---------------|-------------|
| `/register` | POST | ❌ | Register a new user |
| `/login` | POST | ❌ | Login and get JWT token |
| `/episodes` | GET | ❌ | Get all episodes |
| `/episodes/<int:id>` | GET | ❌ | Get episode with appearances |
| `/episodes/<int:id>` | DELETE | ✅ | Delete episode and appearances |
| `/guests` | GET | ❌ | Get all guests |
| `/appearances` | POST | ✅ | Create new appearance |

##  API Documentation

### Episodes

#### Get All Episodes
```http
GET /episodes
```

**Response:**
```json
[
    {
        "id": 1,
        "date": "2024-01-15",
        "number": 1001
    },
    {
        "id": 2,
        "date": "2024-01-16",
        "number": 1002
    }
]
```

#### Get Episode by ID
```http
GET /episodes/1
```

**Response:**
```json
{
    "id": 1,
    "date": "2024-01-15",
    "number": 1001,
    "appearances": [
        {
            "id": 1,
            "rating": 5,
            "guest_id": 1,
            "episode_id": 1,
            "guest": {
                "id": 1,
                "name": "Tom Hanks",
                "occupation": "Actor"
            }
        }
    ]
}
```

#### Delete Episode (Protected)
```http
DELETE /episodes/1
Authorization: Bearer <token>
```

**Response:**
```json
{
    "message": "Episode deleted successfully"
}
```

### Guests

#### Get All Guests
```http
GET /guests
```

**Response:**
```json
[
    {
        "id": 1,
        "name": "Tom Hanks",
        "occupation": "Actor"
    },
    {
        "id": 2,
        "name": "Serena Williams",
        "occupation": "Tennis Player"
    }
]
```

### Appearances

#### Create Appearance (Protected)
```http
POST /appearances
Authorization: Bearer <token>
Content-Type: application/json

{
    "rating": 5,
    "guest_id": 1,
    "episode_id": 1
}
```

**Response:**
```json
{
    "id": 1,
    "rating": 5,
    "guest_id": 1
}