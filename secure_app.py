import sqlite3
import os

# Best Practice: Use Environment Variables for secrets
# To run this, export SECRET_KEY="mysecret" in terminal first
SECRET_KEY = os.getenv("SECRET_KEY", "default_dev_key") 

def login_secure():
    print("\n--- SECURE LOGIN SYSTEM (PATCHED) ---")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # REMEDIATION: Parameterized Queries (Prevents SQL Injection)
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    
    try:
        # Inputs are passed as a tuple, separate from the SQL command
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        
        if user:
            print(">> ACCESS GRANTED")
        else:
            print(">> ACCESS DENIED")
            
    except Exception as e:
        print("An error occurred during login.") # Generic error message (Best Practice)
    finally:
        conn.close()

if __name__ == "__main__":
    login_secure()