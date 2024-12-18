# sql_injection
SQL Injection can allow attackers to view, manipulate, or delete data from your database.
The log messages you're seeing are from your Flask application running in development mode, and they provide useful information about the server's behavior. Let me break down each line for you:

* Running on http://127.0.0.1:5000

Your Flask app is running locally on your machine at http://127.0.0.1:5000. This means you can access the app through a web browser by visiting http://127.0.0.1:5000.
Press CTRL+C to quit

This is a message indicating that you can stop the server by pressing CTRL+C in your terminal.
* Restarting with stat

Flask is running in debug mode, so it automatically reloads the server whenever there is a code change (this is useful during development).
* Debugger is active!

Flask’s debugger is active, which means any errors in the application will be shown in the browser with detailed tracebacks, helping you debug issues.
* Debugger PIN: 128-348-550

This is a security feature Flask provides to prevent unauthorized access to the interactive debugger. If you encounter an error and the debugger is triggered, you'll need to enter this PIN to access it.
127.0.0.1 - - [18/Dec/2024 14:50:59] "GET / HTTP/1.1" 200 -

This log entry shows that a GET request was made to the root URL (/) of your application. The server responded with a 200 status code, which means the request was successful.
127.0.0.1 - - [18/Dec/2024 14:50:59] "GET /favicon.ico HTTP/1.1" 404 -

The browser requested the favicon.ico file (the small icon displayed in the browser tab), but your application doesn’t have this file, so the server responded with a 404 (Not Found) error.
127.0.0.1 - - [18/Dec/2024 14:51:24] "GET /search?name=alice HTTP/1.1" 200 -

A GET request was made to the /search endpoint with the query parameter name=alice. The server responded with a 200 status code, indicating that the request was successful.
127.0.0.1 - - [18/Dec/2024 14:51:31] "GET /search?name=Alice HTTP/1.1" 200 -

A GET request was made to the /search endpoint with the query parameter name=Alice. This is a case-sensitive search, and the server responded with a 200 status code.
127.0.0.1 - - [18/Dec/2024 14:51:47] "GET / HTTP/1.1" 200 -

Another GET request was made to the root URL (/), and the server responded with a 200 status code.
127.0.0.1 - - [18/Dec/2024 14:51:52] "GET /search?name='+OR+1%3D1+-- HTTP/1.1" 200 -

This is the most important log. A malicious SQL injection attempt was made by entering the input '+OR 1=1 --. This input is attempting to exploit the SQL injection vulnerability.
The query formed by the server would be something like:
sql
Copy code
SELECT * FROM users WHERE name = '' OR 1=1 --'
This would make the condition 1=1 always true, and the -- comments out the rest of the query, potentially returning all rows in the users table.
Since you’re still in development mode, this attempt doesn't lead to an error, but it shows that the app is vulnerable to SQL injection.
Summary of What Happened:
The log indicates that someone (or you, testing) tried to perform a SQL injection attack by entering a common SQL injection payload '+OR 1=1 -- in the search input.
The request was processed successfully, but because your application is vulnerable to SQL injection, it could have returned all users from the database.
To fix this, you should use parameterized queries (which I provided earlier) to ensure that user input is treated as data and not executable code.
