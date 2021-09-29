from flask import Flask
from flask import render_template
from flask import *
from markupsafe import Markup
from markupsafe import escape
import connection as conn
import categorySelection as selection

ListaOrdini = []  
ListaAste = []
righeTMP = None

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
    ListaOrdini = conn.estrazioneOridini()
    return render_template('app.html', ListaOrdini = ListaOrdini)

@app.route("/accessori")
def selezione(ListaAste = ListaAste):
    print(str(ListaAste)+"\n\n\n\n\n")
    list.clear(ListaAste)
    ListaAste = selection.accessori(ListaOrdini)
    print(ListaAste)
    return render_template('ast.html', ListaAste = ListaAste)

