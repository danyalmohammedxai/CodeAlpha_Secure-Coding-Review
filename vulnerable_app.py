import sqlite3

def login_vulnerable():
    print("\n--- VULNERABLE LOGIN SYSTEM (DEMO) ---")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    # VULNERABILITY 1: Hardcoded connection string or secrets (Simulated)
    # VULNERABILITY 2: SQL Injection
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    try:
        print(f"[DEBUG] Executing Query: {query}") # Showing query to demonstrate injection
        cursor.execute(query)
        user = cursor.fetchone()
        
        if user:
            print(">> ACCESS GRANTED (Logged in as Admin)")
        else:
            print(">> ACCESS DENIED")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    login_vulnerable()