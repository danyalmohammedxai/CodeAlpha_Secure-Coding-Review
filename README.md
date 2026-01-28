# Secure Coding Review: SQL Injection & Remediation 🛡️
![sql](https://github.com/user-attachments/assets/30a27b7d-0cfb-4f08-980e-b131b81631cf)

### 📋 Project Overview
This project demonstrates the importance of **Secure Coding** by comparing a vulnerable login system with a secured version. It focuses on identifying and patching common web vulnerabilities, specifically **SQL Injection (CWE-89)** and **Hardcoded Credentials (CWE-798)** using Python.

This project was developed as part of a **CodeAlpha Cyber Security Internship** task.

---

### 📂 File Structure

| File Name | Description |
|-----------|-------------|
| `setup_database.py` | Initializes the SQLite database and creates a dummy admin user. |
| `vulnerable_app.py` | Demonstrates unsafe coding practices (vulnerable to SQL Injection). |
| `secure_app.py` | The patched version using **Parameterized Queries** and **Environment Variables**. |

---

### 🚀 How to Run the Project

#### 1. Prerequisites
* Python 3.x installed.
* Terminal or Command Prompt.

#### 2. Clone the Repository
```bash
git clone https://github.com/danyalmohammedxai/CodeAlpha_Secure-Coding-Review.git
cd CodeAlpha_Secure-Coding-Review
```
#### 3. Setup Database
First, initialize the database to create the users.db file and add a default user.

Bash

python setup_database.py
#### 4. Run the Vulnerable Code (Attack Demo)
Run the insecure version to demonstrate an SQL Injection attack.

Bash

python vulnerable_app.py
Attack Payload: Enter admin' OR '1'='1 as the username.

Result: You will bypass the login without a password.

##### 5. Run the Secure Code (Remediation)
Run the secure version to verify the fix.

Bash

python secure_app.py
Test: Try the same payload (admin' OR '1'='1).

Result: Access will be Denied, proving the system is secure.

#### 🔒 Vulnerability Analysis
❌ The Problem (In vulnerable_app.py)
The code uses string concatenation to build SQL queries, which allows attackers to manipulate the database logic.

Python

# Vulnerable Code
query = "SELECT * FROM users WHERE username = '" + username + "'"
✅ The Solution (In secure_app.py)
The code uses Parameterized Queries (Prepared Statements). The database treats user input as data, not executable code.

Python

# Secure Code
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
🧠 Key Concepts
SQL Injection (CWE-89): Occurs when untrusted input is concatenated into SQL queries, allowing attackers to execute arbitrary SQL commands.

Hardcoded Credentials (CWE-798): Storing sensitive data like passwords directly in code, making it easy to extract.

Remediation: Use parameterized queries, input validation, and environment variables for secrets.

Impact: SQL Injection can lead to data theft, modification, or deletion. Hardcoded credentials expose systems to unauthorized access.

🛠 Tools & Technologies
Language: Python 3

Database: SQLite

Concepts: SQL Injection, Secure Coding, Code Review, OWASP Top 10

👤 Author
Danyal Ahmad

Cyber Security Student @ AWKUM

Passionate about Ethical Hacking & Secure Development.

View GitHub Profile

⚠️ Disclaimer
This project is for educational purposes only. The code demonstrates vulnerabilities to help developers understand security risks. Do not use the attack techniques on systems you do not have permission to test.
