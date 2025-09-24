# microsegmentation-honeypot

Microsegmentation Lab with Honeypot

This project demonstrates network microsegmentation and an integrated web honeypot using lightweight containers.
It showcases how isolating services into separate network zones can limit attacker movement while capturing intrusion attempts.

Project Overview

Web Front-End (Nginx): Acts as the public entry point and reverse proxy.

Application API (FastAPI): Business logic layer; only reachable through the web container.

Database Service (SQLite in a Flask wrapper): Runs in its own container to simulate a protected DB segment.

Honeypot (Flask): A fake admin portal that records login attempts and attacker behavior.

By enforcing Docker network rules or external firewall rules, weFeatures

Microsegmentation Demo

Web → App → DB traffic only

DB not directly accessible from the host

Separate honeypot network path

Honeypot Traps

Logs IP, username, password, and timestamp

Simple fake admin UI to attract attackers

Persistent logs for analysis

Containerized & Lightweight

Each service runs in a minimal Python/Nginx image

Ready for Docker Desktop or any Linux host

Tech Stack

Layer	Technology
Reverse Proxy	Nginx
API Layer	FastAPI
Database	SQLite + Flask microservice
Honeypot	Flask
Orchestration	Docker Compose

Repository Layout

microseg-honeypot/
├─ docker-compose.yml
├─ web/        # Nginx front-end
├─ app/        # FastAPI service
├─ db/         # SQLite service with Flask API
└─ honeypot/   # Fake admin portal

