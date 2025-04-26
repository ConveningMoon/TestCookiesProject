# Django Sessions Demo

This project demonstrates how Django sessions work, including creating, accessing, and deleting sessions.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/django-sessions-demo.git
cd django-sessions-demo
```

### 2. Install dependencies with Poetry

```bash
poetry install
```

### 3. Activate the virtual environment

```bash
poetry shell
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Running the Application

```bash
python manage.py runserver
```

### 6. Testing the Session Functionality

Test cookie functionality:

- Visit http://127.0.0.1:8000/session/testcookie/

- Then visit http://127.0.0.1:8000/session/deletecookie/

Create a session:

- Visit http://127.0.0.1:8000/session/create/

Access the session:

- Visit http://127.0.0.1:8000/session/access/

Delete the session:

- Visit http://127.0.0.1:8000/session/delete/

### 7. Folder wth the testing screenshots are in the path `/assets/TestScreenshots`
