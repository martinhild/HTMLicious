from flask import Flask, render_template, request
from datetime import datetime
from berechnungen import berechne_schaltjahre

# Flask initialisieren
app = Flask(__name__)

# Route Startseite aka "/"" aka index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route game.html
@app.route('/game')
def game():
    return render_template('game.html')

# Route schaltjahre.html
@app.route('/schaltjahre', methods=['GET', 'POST'])
def schaltjahre():
    schaltjahre = None  # initialisiert Variable 'schaltjahre'
    if request.method == 'POST':
        # Geburtsdatum aus Form holen (request)
        geburtsdatum = request.form['geburtsdatum']
        if geburtsdatum: # Geburtsdatum existiert
            geburtsjahr = datetime.strptime(geburtsdatum, '%Y-%m-%d').year
            # Funktion aus berechnungen.py
            schaltjahre = berechne_schaltjahre(geburtsjahr)

    # übergebe Schlaltjahre als Variable namens Schaltjahre
    return render_template('schaltjahre.html', schaltjahre=schaltjahre)

# Starte Flask-Server im Debug-Modus
if __name__ == '__main__':
    app.run(debug=True)
