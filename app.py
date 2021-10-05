from flask import Flask
from flask import render_template
from flask import *
from markupsafe import Markup
from markupsafe import escape
import connection as conn
import categorySelection as selection
from datetime import date, datetime

ListaOrdini = []  
ListaAste = []
righeTMP = None
ListaAvvitati = []

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def hello_world(name=None):
    name = Markup("<div>test 2</div>")
    return render_template('app.html', name=name)
    
    
@app.route("/test/<unsecure>")
def test(unsecure):
    name = "<div>THIS IS A TEST</div>"
    return f"<p>{escape(name)}</p>"

@app.route("/generale")
def generale(ListaOrdini = ListaOrdini):
    today = datetime.now()
    ListaOrdini = conn.estrazioneOridini()
    return render_template('app.html', ListaOrdini = ListaOrdini, today = today)

@app.route("/accessori")
def selezioneAccessori(ListaAste = ListaAste):
    today = datetime.now()
    ListaAste = selection.accessori(ListaOrdini)
    return render_template('ast.html', ListaAste = ListaAste, today = today)

@app.route("/avvitati")
def selezioneAvvitati(ListaAvvitati = ListaAvvitati):
    today = datetime.now()
    ListaAvvitati = selection.avvitati(ListaOrdini)
    return render_template('avvitati.html', ListaAvvitati = ListaAvvitati, today = today)