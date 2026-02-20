import sqlite3
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
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
    cur = conn.execute('SELECT * FROM beitraege ORDER BY id DESC')
    rows = cur.fetchall()
    conn.close()

    beitraege = [dict(r) for r in rows]
    return render_template('index.html', beitraege=beitraege)


@app.route('/add', methods=['POST'])
def add_post():
    autor = request.form.get('autor')
    titel = request.form.get('titel')
    inhalt = request.form.get('inhalt')

    if not (autor and titel and inhalt):
        return redirect(url_for('index'))

    conn = get_db_connection()
    conn.execute('INSERT INTO beitraege (autor, titel, inhalt) VALUES (?, ?, ?)', (autor, titel, inhalt))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))


@app.route('/delete/<int:id>', methods=['POST'])
def delete_post(id):
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
