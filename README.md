<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secure Coding Review: SQL Injection & Remediation | CodeAlpha Project</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #0d1b2a; /* Deep Navy */
            --secondary: #1b263b; /* Dark Blue */
            --accent: #00d4aa; /* Teal Green */
            --danger: #e63946; /* Red */
            --warning: #f77f00; /* Orange */
            --text-light: #f1faee; /* Off-White */
            --text-dark: #1d3557; /* Dark Blue-Gray */
            --bg-card: rgba(255, 255, 255, 0.98);
            --shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        }
        
        * { box-sizing: border-box; }
        
        body { 
            font-family: 'Roboto', sans-serif; 
            margin: 0; 
            padding: 0; 
            color: var(--text-dark); 
            line-height: 1.7;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            background-attachment: fixed;
            overflow-x: hidden;
        }
        
        /* Header with Gradient and Animation */
        header { 
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: var(--text-light); 
            padding: 60px 20px; 
            text-align: center; 
            position: relative;
            box-shadow: var(--shadow);
            animation: fadeIn 1s ease-in;
        }
        header h1 { 
            margin: 0; 
            font-size: 3em; 
            font-weight: 700; 
            text-transform: uppercase; 
            letter-spacing: 3px; 
            text-shadow: 0 0 20px rgba(0, 212, 170, 0.5);
        }
        header p { 
            font-size: 1.3em; 
            margin: 10px 0; 
            opacity: 0.9;
        }
        header .subtitle { 
            font-size: 0.9em; 
            color: var(--accent); 
            font-weight: 500;
        }
        
        /* Navigation Menu */
        nav { 
            background: var(--secondary); 
            padding: 10px 0; 
            text-align: center; 
            position: sticky; 
            top: 0; 
            z-index: 100; 
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }
        nav a { 
            color: var(--text-light); 
            text-decoration: none; 
            margin: 0 20px; 
            font-weight: 500; 
            transition: color 0.3s;
        }
        nav a:hover { color: var(--accent); }
        
        .container { 
            max-width: 1100px; 
            margin: auto; 
            padding: 40px 20px; 
        }
        
        /* Module Cards with Enhanced Styling */
        .module-card { 
            background: var(--bg-card); 
            margin-bottom: 40px; 
            padding: 30px; 
            border-radius: 12px; 
            box-shadow: var(--shadow); 
            border-left: 6px solid var(--accent);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        .module-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, var(--accent), var(--warning));
        }
        .module-card:hover {
            transform: translateY(-8px) scale(1.02); 
            box-shadow: 0 12px 40px rgba(0,0,0,0.3);
        }
        
        h2 { 
            color: var(--primary); 
            font-size: 1.8em; 
            margin-bottom: 20px; 
            font-weight: 600; 
            border-bottom: 3px solid var(--accent); 
            padding-bottom: 10px;
        }
        
        /* Stats and Alerts */
        .stat-box { 
            background: linear-gradient(135deg, #e3f2fd, #bbdefb); 
            padding: 20px; 
            border-radius: 8px;
            text-align: center; 
            font-weight: 600; 
            color: var(--primary); 
            margin: 20px 0; 
            border: 1px solid var(--accent);
        }
        .red-flag { 
            color: var(--danger); 
            font-weight: 700; 
            background: rgba(230, 57, 70, 0.1); 
            padding: 2px 6px; 
            border-radius: 4px;
        }
        .green-flag { 
            color: #2d6a4f; 
            font-weight: 700; 
            background: rgba(45, 106, 79, 0.1); 
            padding: 2px 6px; 
            border-radius: 4px;
        }
        
        /* Code Blocks */
        .code-block { 
            background: #f8f9fa; 
            padding: 15px; 
            border-radius: 8px; 
            border: 1px solid #e9ecef; 
            font-family: 'Courier New', monospace; 
            margin: 15px 0; 
            overflow-x: auto;
        }
        .code-block pre { margin: 0; white-space: pre-wrap; }
        
        /* Tables */
        table { 
            width: 100%; 
            border-collapse: collapse; 
            margin: 20px 0; 
            background: var(--bg-card); 
            border-radius: 8px; 
            overflow: hidden; 
            box-shadow: var(--shadow);
        }
        th, td { 
            padding: 12px; 
            text-align: left; 
            border-bottom: 1px solid #ddd; 
        }
        th { 
            background: var(--accent); 
            color: white; 
            font-weight: 600;
        }
        tr:hover { background: rgba(0, 212, 170, 0.1); }
        
        /* Lists */
        ul, ol { padding-left: 20px; }
        li { margin-bottom: 10px; }
        
        /* Buttons and CTAs */
        .cta-button { 
            display: inline-block; 
            background: var(--accent); 
            color: white; 
            padding: 12px 24px; 
            text-decoration: none; 
            border-radius: 6px; 
            font-weight: 600; 
            transition: background 0.3s;
            margin-top: 20px;
        }
        .cta-button:hover { background: var(--warning); }
        
        /* Footer */
        footer { 
            text-align: center; 
            padding: 30px; 
            background: var(--primary); 
            color: var(--text-light); 
            margin-top: 60px; 
            border-top: 3px solid var(--accent);
        }
        
        /* Animations */
        @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        .module-card { animation: fadeIn 0.8s ease-out; }
        
        /* Responsive */
        @media (max-width: 768px) {
            header h1 { font-size: 2.2em; }
            nav a { display: block; margin: 10px 0; }
            .container { padding: 20px 15px; }
            table { font-size: 0.9em; }
        }
    </style>
</head>
<body>

    <header>
        <h1>Secure Coding Review: SQL Injection & Remediation</h1>
        <p>Interactive Cyber Security Module</p>
        <p class="subtitle">CodeAlpha Cyber Security Internship Task | Developed by Danyal Ahmad</p>
    </header>

    <nav>
        <a href="#overview">Overview</a>
        <a href="#structure">File Structure</a>
        <a href="#setup">Setup</a>
        <a href="#vulnerable">Vulnerable Code</a>
        <a href="#secure">Secure Code</a>
        <a href="#analysis">Analysis</a>
        <a href="#tools">Tools</a>
        <a href="#author">Author</a>
    </nav>

    <div class="container">

        <div id="overview" class="module-card">
            <h2>📋 Project Overview</h2>
            <p>This project demonstrates the importance of <strong>Secure Coding</strong> by comparing a vulnerable login system with a secured version. It focuses on identifying and patching common web vulnerabilities, specifically <strong>SQL Injection (CWE-89)</strong> and <strong>Hardcoded Credentials (CWE-798)</strong> using Python.</p>
            <p>This project was developed as part of a <strong>CodeAlpha Cyber Security Internship</strong> task.</p>
            <div class="stat-box">🛡️ Secure coding prevents 90% of common web vulnerabilities like SQL Injection.</div>
        </div>

        <div id="structure" class="module-card">
            <h2>📂 File Structure</h2>
            <table>
                <thead>
                    <tr>
                        <th>File Name</th>
                        <th>Description</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><code>setup_database.py</code></td>
                        <td>Initializes the SQLite database and creates a dummy admin user.</td>
                    </tr>
                    <tr>
                        <td><code>vulnerable_app.py</code></td>
                        <td>Demonstrates unsafe coding practices (vulnerable to SQL Injection).</td>
                    </tr>
                    <tr>
                        <td><code>secure_app.py</code></td>
                        <td>The patched version using <strong>Parameterized Queries</strong> and <strong>Environment Variables</strong>.</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div id="setup" class="module-card">
            <h2>🚀 How to Run the Project</h2>
            <h3>1. Prerequisites</h3>
            <ul>
                <li>Python 3.x installed.</li>
                <li>Terminal or Command Prompt.</li>
            </ul>
            <h3>2. Clone the Repository</h3>
            <div class="code-block">
                <pre>git clone https://github.com/danyalmohammedxai/CodeAlpha_Secure-Coding-Review.git
cd CodeAlpha_Secure-Coding-Review</pre>
            </div>
            <h3>3. Setup Database</h3>
            <p>First, initialize the database to create the users.db file and add a default user.</p>
            <div class="code-block">
                <pre>python setup_database.py</pre>
            </div>
            <h3>4. Run the Vulnerable Code (Attack Demo)</h3>
            <p>Run the insecure version to demonstrate an SQL Injection attack.</p>
            <div class="code-block">
                <pre>python vulnerable_app.py</pre>
            </div>
            <p><strong>Attack Payload:</strong> Enter <code>admin' OR '1'='1</code> as the username.</p>
            <p><strong>Result:</strong> You will bypass the login without a password.</p>
            <h3>5. Run the Secure Code (Remediation)</h3>
            <p>Run the secure version to verify the fix.</p>
            <div class="code-block">
                <pre>python secure_app.py</pre>
            </div>
            <p><strong>Test:</strong> Try the same payload (<code>admin' OR '1'='1</code>).</p>
            <p><strong>Result:</strong> Access will be Denied, proving the system is secure.</p>
        </div>

        <div id="vulnerable" class="module-card">
            <h2>❌ The Problem (In vulnerable_app.py)</h2>
            <p>The code uses string concatenation to build SQL queries, which allows attackers to manipulate the database logic.</p>
            <div class="code-block">
                <pre># Vulnerable Code
query = "SELECT * FROM users WHERE username = '" + username + "'"</pre>
            </div>
            <p>This leads to SQL Injection, where malicious input alters the query structure.</p>
        </div>

        <div id="secure" class="module-card">
            <h2>✅ The Solution (In secure_app.py)</h2>
            <p>The code uses <strong>Parameterized Queries (Prepared Statements)</strong>. The database treats user input as data, not executable code.</p>
            <div class="code-block">
                <pre># Secure Code
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))</pre>
            </div>
            <p>This prevents injection by separating code from data.</p>
        </div>

        <div id="analysis" class="module-card">
            <h2>🔒 Vulnerability Analysis</h2>
            <p><span class="red-flag">SQL Injection (CWE-89):</span> Occurs when untrusted input is concatenated into SQL queries, allowing attackers to execute arbitrary SQL commands.</p>
            <p><span class="red-flag">Hardcoded Credentials (CWE-798):</span> Storing sensitive data like passwords directly in code, making it easy to extract.</p>
            <p><span class="green-flag">Remediation:</span> Use parameterized queries, input validation, and environment variables for secrets.</p>
            <p><strong>Impact:</strong> SQL Injection can lead to data theft, modification, or deletion. Hardcoded credentials expose systems to unauthorized access.</p>
        </div>

        <div id="tools" class="module-card">
            <h2>🛠 Tools & Technologies</h2>
            <ul>
                <li><strong>Language:</strong> Python 3</li>
                <li><strong>Database:</strong> SQLite</li>
                <li><strong>Concepts:</strong> SQL Injection, Secure Coding, Code Review, OWASP Top 10</li>
            </ul>
        </div>

        <div id="author" class="module-card">
            <h2>👤 Author</h2>
            <p><strong>Danyal Ahmad</strong></p>
            <p>Cyber Security Student @ AWKUM</p>
            <p>Passionate about Ethical Hacking & Secure Development.</p>
            <a href="https://github.com/danyalmohammedxai" class="cta-button" target="_blank">View GitHub</a>
        </div>

        <div class="module-card">
            <h2>⚠️ Disclaimer</h2>
            <p>This project is for educational purposes only. The code demonstrates vulnerabilities to help developers understand security risks. Do not use the attack techniques on systems you do not have permission to test.</p>
        </div>

    </div>

    <footer>
        <p>&copy; 2026 Secure Coding Review Module | CodeAlpha Project by Danyal Ahmad.</p>
    </footer>

</body>
</html>
