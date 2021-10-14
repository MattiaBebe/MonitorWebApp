from flask import Flask
from flask import render_template
from flask import *
from markupsafe import Markup
from markupsafe import escape
import connection as conn
import categorySelection as selection
from datetime import date, datetime
from bokeh.plotting import figure, show, output_file, save
from bokeh.resources import CDN
from bokeh.embed import file_html

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]


ListaOrdini = []  
ListaAste = []
righeTMP = None
ListaAvvitati = []
ListaDati = []
ListaDatiOrdine = []
ListaPremontaggi = []

app = Flask(__name__)

# create a new plot with a title and axis labels
p = figure(title="Simple line example", x_axis_label="x", y_axis_label="y")

# add a line renderer with legend and line thickness
p.line(x, y, legend_label="Temp.", line_width=2)

grafico = save(p)
visualizzazioneGrafico = show(p)

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

#route per la vista per tabella dati 

@app.route("/dati")
def selezioneAvv(ListaDati = ListaDati):
    ListaDati = conn.estrazioneDati()
    return render_template('dati.html', ListaDati = ListaDati)

#route per la visualizzazione dettagli ordine 

@app.route("/vistaOrdine/<ordine>")
def vistaOrdine(ordine, ListaDatiOrdine = ListaDatiOrdine):
    ListaDatiOrdine = conn.datiOrdine(ordine) 
    for i in ListaDatiOrdine:
         i['bdmng'] = str(i['bdmng']).split('.')[0] 
    return render_template('vistaOrdine.html', ordine = ordine, ListaDatiOrdine = ListaDatiOrdine)

#route per vista dei premontaggi ISO

@app.route("/premontaggio")
def vistaPremontaggi():
    selection.premontaggi()
    return render_template("premontaggio.html", ListaPre = ListaPremontaggi)

#routes per viste montaggi IS2, AVV, KTR, XF

@app.route("/monaggio")
def vistaMontaggio():

    return render_template("montaggio.html")