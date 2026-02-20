import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from pathlib import Path

app = Flask(__name__)

# Database file next to this script
DB_PATH = Path(__file__).parent / 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET'])
def index():
    conn = get_db_connection()
    beitraege = conn.execute('SELECT * FROM beitraege ORDER BY id DESC').fetchall()
    text_quiz = conn.execute('SELECT * FROM text_quiz').fetchall()
    conn.close()
    return render_template('index.html', beitraege=beitraege, text_quiz=text_quiz)


@app.route('/add', methods=['POST'])
def add_post():
    # Check if it's a beitrag (Schwarzes Brett)
    autor = request.form.get('autor')
    titel = request.form.get('titel')
    inhalt = request.form.get('inhalt')
    
    # Check if it's a quiz question
    frage1 = request.form.get('frage1')
    antwort1 = request.form.get('antwort1')
    frage2 = request.form.get('frage2')
    antwort2 = request.form.get('antwort2')
    
    conn = get_db_connection()
    
    if autor and titel and inhalt:
        conn.execute('INSERT INTO beitraege (autor, titel, inhalt) VALUES (?, ?, ?)', (autor, titel, inhalt))
        conn.commit()
    
    if frage1 and antwort1 and frage2 and antwort2:
        conn.execute("INSERT INTO text_quiz (frage1, antwort1, frage2, antwort2) VALUES (?, ?, ?, ?)",
                     (frage1, antwort1, frage1, antwort2))
        conn.commit()
    
    conn.close()
    return redirect(url_for('index'))


@app.route('/delete_beitrag/<int:id>', methods=['POST'])
def delete_beitrag(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM beitraege WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route("/start")
def start():
    return render_template('start.html')


@app.route("/schüler")
def schüler():
    return render_template('schüler.html')


@app.route('/add_schueler', methods=['POST'])
def add_schueler():
    name = request.form.get('name')
    klasse = request.form.get('klasse')
    
    if not (name and klasse):
        return redirect(url_for('schüler'))
    
    conn = get_db_connection()
    conn.execute('INSERT INTO schueler (name, klasse) VALUES (?, ?)', (name, klasse))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
