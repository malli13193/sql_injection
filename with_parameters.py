@app.route('/search')
def search():
    name = request.args.get('name')

    # Secure SQL query (no SQL injection)
    conn = sqlite3.connect('vulnerable_app.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = ?"  # Use parameterized queries
    cursor.execute(query, (name,))
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
