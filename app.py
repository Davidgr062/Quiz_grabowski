from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Daten aus dem Formular auslesen (nutzt das 'name'-Attribut aus HTML)
        nutzername = request.form.get('nutzername')
        return f"Hallo {nutzername}, deine Daten wurden empfangen!"

    # Wenn die Seite normal aufgerufen wird (GET)
    return render_template('index.html')