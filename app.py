import sqlite3
from flask import Flask, render_template, request, redirect, url_for
 
app = Flask(__name__)
 
# Datenbank-Verbindung
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
 
# Startseite
@app.route('/')
def start():
    return render_template('start.html')

# Lehrer-Seite / Board anzeigen
@app.route('/lehrer')
def index():
    conn = get_db_connection()
    text_quiz = conn.execute('SELECT * FROM text_quiz').fetchall()
    conn.close()
    return render_template('index.html', text_quiz=text_quiz)
 
# Quiz-Seite: Fragen anzeigen und beantworten
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    conn = get_db_connection()
    text_quiz = conn.execute('SELECT * FROM text_quiz').fetchall()
   
    if request.method == 'POST':
        # Antworten überprüfen
        erstelltes_Quiz  = []
        for quiz in text_quiz:
            frage1_id = quiz['Id']
            frage2_id = quiz['Id']
           
            user_antwort1 = request.form.get(f'antwort1_{frage1_id}', '').strip()
            user_antwort2 = request.form.get(f'antwort2_{frage2_id}', '').strip()
           
            correct1 = user_antwort1.lower() == quiz['antwort1'].lower()
            correct2 = user_antwort2.lower() == quiz['antwort2'].lower()
            
            erstelltes_Quiz.append({
                'frage1': quiz['frage1'],
                'antwort1': quiz['antwort1'],
                'user_antwort1': user_antwort1,
                'correct1': correct1,
                'frage2': quiz['frage2'],
                'antwort2': quiz['antwort2'],
                'user_antwort2': user_antwort2,
                'correct2': correct2
            })
       
        conn.close()
        return render_template('quiz.html', text_quiz=text_quiz, erstelltes_Quiz=erstelltes_Quiz )
    
    conn.close()
    return render_template('quiz.html', text_quiz=text_quiz)
 
# Neue Nachricht hinzufügen
@app.route('/add', methods=['POST'])
def add_post():
    quiz_titel = request.form.get('quiz_titel')
    frage1 = request.form.get('frage1')
    antwort1 = request.form.get('antwort1')
    frage2 = request.form.get('frage2')
    antwort2 = request.form.get('antwort2')
 
    if frage1 and antwort1 and frage2 and antwort2 and quiz_titel:
        conn = get_db_connection()
        conn.execute("INSERT INTO text_quiz (frage1, antwort1, frage2, antwort2, quiz_titel) VALUES (?, ?, ?, ?, ?)",
                     (frage1, antwort1, frage2, antwort2, quiz_titel))
        conn.commit()
        conn.close()
 
    return redirect(url_for('index'))
 
# Nachricht löschen
@app.route('/delete/<int:id>', methods=['POST'])
def delete_post(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM text_quiz WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
 
if __name__ == '__main__':
    app.run(debug=True)