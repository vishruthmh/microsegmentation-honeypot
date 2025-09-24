# Microsegmentation-Honeypot

**Microsegmentation Lab with Honeypot**

This project demonstrates **network microsegmentation** and an integrated **web honeypot** using lightweight containers.  
It shows how isolating services into separate network zones can limit attacker movement while capturing intrusion attempts.

---

## Project Overview
- **Web Front-End (Nginx):** Public entry point and reverse proxy.  
- **Application API (FastAPI):** Business logic layer; reachable only through the web container.  
- **Database Service (SQLite + Flask wrapper):** Runs in its own container to simulate a protected DB segment.  
- **Honeypot (Flask):** Fake admin portal that records login attempts and attacker behavior.

By enforcing Docker network rules or external firewall rules, each component communicates **only with approved neighbors**.

---

##  Features
### Microsegmentation Demo
- Web → App → DB traffic only  
- DB not directly accessible from the host  
- Separate honeypot network path

### Honeypot Traps
- Logs IP, username, password, and timestamp  
- Simple fake admin UI to attract attackers  
- Persistent logs for analysis

### Containerized & Lightweight
- Each service runs in a minimal Python/Nginx image  
- Ready for Docker Desktop or any Linux host

---

## Tech Stack
| Layer          | Technology              |
|----------------|-------------------------|
| Reverse Proxy  | **Nginx**               |
| API Layer      | **FastAPI**             |
| Database       | **SQLite + Flask API**  |
| Honeypot       | **Flask**               |
| Orchestration  | **Docker Compose**      |

---

## 📂 Repository Layout

```text
microseg-honeypot/
├── docker-compose.yml         # Docker orchestration for all services
├── web/                       # Nginx front-end reverse proxy
├── app/                       # FastAPI service (core application logic)
├── db/                        # SQLite service with Flask API wrapper
└── honeypot/                  # Fake admin portal (honeypot interface)

