from flask import Flask, render_template, request, redirect, send_file
import sqlite3
import csv
import os

app = Flask(__name__)

# Connect to SQLite DB
def get_db_connection():
    conn = sqlite3.connect('tickets.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create tickets table
def create_table():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS tickets
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     title TEXT,
                     description TEXT,
                     priority TEXT,
                     status TEXT)''')
    conn.commit()
    conn.close()

create_table()

# Home page: show all tickets
@app.route('/')
def index():
    conn = get_db_connection()
    # Open tickets first, then closed
    tickets = conn.execute('SELECT * FROM tickets ORDER BY CASE status WHEN "Closed" THEN 1 ELSE 0 END, id').fetchall()
    conn.close()
    return render_template('index.html', tickets=tickets)

# Add ticket
@app.route('/add', methods=('GET','POST'))
def add_ticket():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        priority = auto_priority(description)
        status = 'Open'

        conn = get_db_connection()
        conn.execute('INSERT INTO tickets (title, description, priority, status) VALUES (?, ?, ?, ?)',
                     (title, description, priority, status))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add_ticket.html')

# Update ticket
@app.route('/update/<int:id>', methods=('GET','POST'))
def update_ticket(id):
    conn = get_db_connection()
    ticket = conn.execute('SELECT * FROM tickets WHERE id=?', (id,)).fetchone()

    if request.method == 'POST':
        new_status = request.form['status']
        new_priority = request.form['priority']
        conn.execute('UPDATE tickets SET status=?, priority=? WHERE id=?', (new_status, new_priority, id))
        conn.commit()
        conn.close()
        return redirect('/')

    conn.close()
    return render_template('update_ticket.html', ticket=ticket)

# Export tickets to CSV
@app.route('/export')
def export_tickets():
    conn = get_db_connection()
    tickets = conn.execute('SELECT * FROM tickets').fetchall()
    conn.close()

    filename = 'tickets.csv'
    filepath = os.path.join(os.getcwd(), filename)

    # Write CSV file
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Title', 'Description', 'Priority', 'Status'])  # Header
        for t in tickets:
            writer.writerow([t['id'], t['title'], t['description'], t['priority'], t['status']])

    return send_file(filepath, as_attachment=True)

# Auto-priority logic
def auto_priority(description):
    description = description.lower()
    if 'urgent' in description or 'server' in description or 'crash' in description:
        return 'High'
    elif 'slow' in description or 'error' in description:
        return 'Medium'
    else:
        return 'Low'

if __name__ == '__main__':
    app.run(debug=True)

