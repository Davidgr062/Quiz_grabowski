import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Datenbank-Verbindung
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Startseite / Board anzeigen
@app.route('/')
def index():
    conn = get_db_connection()
    text_quiz = conn.execute('SELECT * FROM text_quiz').fetchall()
    conn.close()
    return render_template('index.html', text_quiz=text_quiz)

# Neue Nachricht hinzufügen
@app.route('/add', methods=['POST'])
def add_post():
    frage1 = request.form.get('frage1')
    antwort1 = request.form.get('antwort1')
    frage2 = request.form.get('frage2')
    antwort2 = request.form.get('antwort2')

    if frage1 and antwort1 and frage2 and antwort2:
        conn = get_db_connection()
        conn.execute("INSERT INTO text_quiz (frage1, antwort1, frage2, antwort2) VALUES (?, ?, ?, ?)",
                     (frage1, antwort1, frage1, antwort2))
        conn.commit()
        conn.close()

    return redirect(url_for('index'))

# Nachricht löschen
#@app.route('/delete/<int:id>', methods=['POST'])
#def delete_post(id):
   # conn = get_db_connection()
   # conn.execute('DELETE FROM text_quiz WHERE id = ?', (id,))
   # conn.commit()
   # conn.close()
   # return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
