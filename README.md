# Student Virtual Assistant

![Status](https://img.shields.io/badge/status-archived-red)
![Python](https://img.shields.io/badge/python-3-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-black?logo=flask&logoColor=white)
![Vue](https://img.shields.io/badge/vue-3-4FC08D?logo=vuedotjs&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-database-4479A1?logo=mysql&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-yellow)

>**Archived project.** This repository is no longer maintained and some files were removed for privacy reasons before it was published. Some functionality may not work exactly as intended: the code is provided as-is for reference and portfolio purposes.

A web application built for students of the **University of Geneva (UNIGE)** to help them organize their academic life in one place: class schedules, assignments/tasks, revisions, and exam periods, all synced with the university's official course catalog (PGC).

Developed by **Lázár Barta** (backend) and **Laila Laaris** (frontend)
@ Université de Genève – DiSTIC, October–December 2022

**Demo video:** https://youtu.be/WEbyHLGcyhA

---

## Table of contents

- [Overview](#overview)
- [Features](#features)
- [Tech stack](#tech-stack)
- [Project structure](#project-structure)
- [Getting started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Database setup](#1-database-setup)
  - [Backend setup](#2-backend-setup)
  - [Frontend setup](#3-frontend-setup)
- [API documentation](#api-documentation)
- [Known limitations](#known-limitations)
- [Contact](#contact)
- [License](#license)

---

## Overview

The Student Virtual Assistant lets a student:

- Register/log in with an account tied to their curriculum (`cursus`).
- Add courses either manually or by searching the university's official schedule (PGC, *Programme des cours de Genève*), which automatically generates the corresponding recurring class sessions.
- View all class sessions and personal events in a calendar (day/week views).
- Manage a to-do list of tasks (readings, exercises/TPs, revisions...) linked to courses, with due dates, states and completion status.
- Mark a period as a holiday/break, which clears events and course-related tasks in that range while keeping personal ones.
- Track course-related checklists (courses covered, TPs, readings, revisions) per class.

The project is split into two independent parts that talk to each other over a REST API:

- **Backend** (`/`, `Implementation/`): a Python/Flask API backed by MySQL.
- **Frontend** (`interface/`): a Vue 3 single-page application.

## Features

- 🔐 User signup / login
- 📅 Interactive calendar (built with FullCalendar) showing courses and personal events
- 📚 Course management (add/edit/delete), including lookup against the official UNIGE course catalog
- ✅ Task/checklist management per course (status, state, due dates)
- 🏖️ Holiday/break handling that cleans up the schedule automatically
- 🧑‍🎓 Student profile info

## Tech stack

| Layer      | Technology |
|------------|------------|
| Frontend   | Vue 3, Vue Router, Vuex, Vuetify, Bootstrap-Vue, FullCalendar, Axios |
| Backend    | Python 3, Flask, Flask-CORS |
| Database   | MySQL |
| Tooling    | Vue CLI, npm |

## Project structure

```
student-virtual-assistant/
├── api.py                        # Flask application entry point (routes/endpoints)
├── SQL_dump/
│   └── assistant-etudiant.sql    # Database schema + seed data (dump to import)
├── API_endpoints/
│   ├── endpoints.md              # Full API reference (methods, params, bodies)
│   └── api_testing.http          # Sample HTTP requests for manual testing
├── Implementation/
│   ├── Methods/
│   │   ├── API_methods/          # One file per endpoint's business logic
│   │   ├── Instaciations/        # Turns a course schedule into concrete calendar events
│   │   ├── Parsing/              # Parses the UNIGE course catalog (PGC) and events
│   │   ├── SQL_requests/         # Centralized SQL queries
│   │   └── Utils/                # Shared backend helpers
│   ├── Utils/                    # Response helpers, status codes, semester dates
│   └── SQL_dump/                 # (duplicate copy of the SQL dump)
└── interface/                    # Vue 3 frontend application
    ├── src/
    │   ├── views/                 # Page-level components (Calendar, Courses, Tasks, Login, Signup...)
    │   ├── components/            # Reusable UI components (NavBar, Calendar widget, lists...)
    │   ├── router/                # Vue Router routes
    │   ├── store/                 # Vuex store
    │   └── plugins/               # Vuetify / webfontloader setup
    └── package.json
```

## Getting started

### Prerequisites

- Python 3
- [Flask](https://flask.palletsprojects.com/) and [Flask-CORS](https://flask-cors.readthedocs.io/)
- MySQL Server
- Node.js and npm

### 1. Database setup

1. Create a MySQL database named `assistant-etudiant`.
2. Import the provided SQL dump into it:
   ```bash
   mysql -u root -p assistant-etudiant < SQL_dump/assistant-etudiant.sql
   ```
   This creates all required tables (`USER`, `TASKS`, `SCHEDULE`, `EVENT_DATE`, `UNIGE_COURSES`, etc.) and seeds the `UNIGE_COURSES` table with the official UNIGE course list for the 2022–2023 academic year.
3. If you need to refresh the course catalog for a different year, truncate the `UNIGE_COURSES` table and re-run the parser:
   ```bash
   python Implementation/Methods/Parsing/parse.py
   ```
4. By default the backend connects with `host='localhost'`, `user='root'`, `password=''` (see `cnx()` in `api.py`). Update these credentials there if your local MySQL setup differs.

### 2. Backend setup

From the project root:

```bash
# install the required Python packages, e.g.
pip install flask flask-cors mysql-connector-python

# run the server
export FLASK_APP=api.py
flask run
```

The API will be served at `http://127.0.0.1:5000` by default.

### 3. Frontend setup

From the `interface/` directory:

```bash
cd interface

# install dependencies
npm install

# run a local dev server with hot-reload
npm run serve

# or build a production bundle
npm run build
```

The frontend expects the backend API to be reachable (CORS is enabled on the Flask side for all origins).

## API documentation

The full list of endpoints (HTTP methods, query parameters, request/response bodies) is documented in [`API_endpoints/endpoints.md`](API_endpoints/endpoints.md). A ready-to-use collection of sample requests is also available in [`API_endpoints/api_testing.http`](API_endpoints/api_testing.http) (usable with the VS Code REST Client extension or similar tools).

At a high level, endpoints are organized under a per-user path `/{id}/...` and cover:

- `/{id}/course/data`: list, create, update or delete courses
- `/{id}/course/tasks/data`: create, update, or change the status/state of tasks
- `/{id}/schedules/data/pgc`: search the official UNIGE course catalog
- `/{id}/tasks/data`, `/{id}/events/data`: read/delete tasks and calendar events
- `/{id}/events/holiday/data`: declare a holiday period
- `/{id}/infos/data`: get the logged-in student's profile info
- `/connection/data`, `/signup/data`: login and account creation

## Known limitations

As noted at the top of this file, this repository is an **archived, academic (school project) snapshot**:

- Some files were stripped out before publishing for privacy reasons, so parts of the app may not run out of the box.
- Secrets/credentials in the code (e.g. the Flask `secret_key`, default DB credentials) are placeholders from development and **must not** be reused as-is.
- The project was built as a time-boxed university assignment (Oct–Dec 2022) rather than a production system, so error handling, security hardening and test coverage are minimal.

## Contact

For further assistance, feel free to reach out:

- **Backend**: Lázár Barta, Lazar.Barta@unige.ch
- **Frontend**: Laila Laaris, Laila.Laaris@unige.ch

or through GitHub.

## License

This project is licensed under the [MIT License](LICENSE).
