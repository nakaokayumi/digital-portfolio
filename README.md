# digital-portfolio
# 🛡️ Secure Identity & Access Management (IAM) Portal
> **Project Goal:** To engineer a robust, audit-ready authentication gateway that mitigates OWASP Top 10 vulnerabilities.

---

## 🚀 Overview
This project is a functional IAM portal built with **Python (Flask)**. It was designed with a "Security-First" mindset, focusing on protecting user credentials and ensuring administrative transparency—critical pillars for high-scale platforms like **Grab**.

## 🛡️ Security Features
* **Cryptographic Hashing:** Utilizes **PBKDF2 with SHA-256** salting to ensure password data is computationally infeasible to crack.
* **SQL Injection (SQLi) Prevention:** Implemented strictly **parameterized queries** for all database interactions.
* **Session Management:** Secure cookie handling to prevent session hijacking and unauthorized access.
* **PDPA-Compliant Audit Logging:** Automated logging of all authentication events (success/failure) for forensic traceability and regulatory compliance.

## 🛠️ Tech Stack
* **Backend:** Python 3, Flask
* **Database:** SQLite
* **Frontend:** HTML5, CSS3 (High-contrast Dark Mode for Analyst UX)
* **Version Control:** Git

## 📂 Project Structure
```bash
├── app.py              # Main application logic & Security Middlewares
├── database.db         # SQLite instance (Encrypted/Salted storage)
├── templates/          # Secure UI components
├── static/             # CSS (Red/Black Theme)
└── logs/               # Audit trail for PDPA compliance
