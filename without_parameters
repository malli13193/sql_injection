from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Initialize SQLite database and create a table if it doesn't exist
def init_db():
    conn = sqlite3.connect('vulnerable_app.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
    ''')
    conn.commit()

    # Insert some data (only if the table is empty)
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
        cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
        cursor.execute("INSERT INTO users (name, age) VALUES ('Charlie', 35)")
        conn.commit()
    conn.close()

# Initialize the database
init_db()

# Home page where user can search for a user by name (vulnerable to SQL injection)
@app.route('/')
def home():
    return '''
        <h1>Search for a User</h1>
        <form action="/search" method="get">
            Name: <input type="text" name="name">
            <input type="submit" value="Search">
        </form>
    '''

# Search page that is vulnerable to SQL injection
@app.route('/search')
def search():
    name = request.args.get('name')
    
    # Vulnerable SQL query (SQL injection possible)
    conn = sqlite3.connect('vulnerable_app.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE name = '{name}'"  # SQL injection vulnerability
    cursor.execute(query)
    users = cursor.fetchall()
    conn.close()

    return render_template_string("""
        <h1>Search Results</h1>
        {% if users %}
            <ul>
                {% for user in users %}
                    <li>{{ user[1] }} ({{ user[2] }} years old)</li>
                {% endfor %}
            </ul>
        {% else %}
            <p>No users found.</p>
        {% endif %}
        <a href="/">Go back</a>
    """, users=users)

if __name__ == '__main__':
    app.run(debug=True)
