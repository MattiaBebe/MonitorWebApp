from connection import AstList, ListaDati, ListaDatiOrdine
import connection as conn
import app as ap

AccList = []
AvvList = []
ListaPremontaggi = []
ListaMontaggio = []

def accessori(ListaOrdini):
    AccList.clear()
    print(AccList)
    for i in ListaOrdini:
        if str(i['cate']) == 'ACC':
            dictionaryAstList = {
                                "chiave" : None,
                                "ordine" : None,
                                "qta" : None,
                                "cance" : None,
                                "errore" : None,
                                "data" : None,
                                "codice" : None,
                                "cliente" : None,
                                "cate" : None,
                                "codcli" : None,
                                "vornr" : None,
                                "AUFPL" : None,
                                "dipe" : None,
                                "tempo" : None,
                                "ARBID" : None
                             }
            dictionaryAstList["chiave"] = i['chiave']
            dictionaryAstList["ordine"] = i['ordine']
            dictionaryAstList["qta"] = i['qta']
            dictionaryAstList["cance"] = i['cance']
            dictionaryAstList["errore"] = i['errore']
            dictionaryAstList["data"] = i['data']
            dictionaryAstList["codice"] = i['codice']
            dictionaryAstList["cliente"] = i['cliente']
            dictionaryAstList["cate"] = i['cate']
            dictionaryAstList["codcli"] = i['codcli']
            dictionaryAstList["vornr"] = i['vornr']
            dictionaryAstList["AUFPL"] = i['AUFPL']
            dictionaryAstList["dipe"] = i['dipe']
            dictionaryAstList["tempo"] = i['tempo']
            dictionaryAstList["ARBID"] = i['ARBID']
            AccList.append(dictionaryAstList)    
    if AccList == ap.ListaAste:
        print("lista già aggiornata")
        return
    else:
        list.clear(ap.ListaAste)
        print("sono dento l'else")
        print(ap.ListaAste)
        return(AccList)

def avvitati(ListaOrdini):
    AvvList.clear()
    for i in ListaOrdini:
        if str(i['cate']) == 'AVV':
            dictionaryAvvList = {
                                "chiave" : None,
                                "ordine" : None,
                                "qta" : None,
                                "cance" : None,
                                "errore" : None,
                                "data" : None,
                                "codice" : None,
                                "cliente" : None,
                                "cate" : None,
                                "codcli" : None,
                                "vornr" : None,
                                "AUFPL" : None,
                                "dipe" : None,
                                "tempo" : None,
                                "ARBID" : None
                             }
            dictionaryAvvList["chiave"] = i['chiave']
            dictionaryAvvList["ordine"] = i['ordine']
            dictionaryAvvList["qta"] = i['qta']
            dictionaryAvvList["cance"] = i['cance']
            dictionaryAvvList["errore"] = i['errore']
            dictionaryAvvList["data"] = i['data']
            dictionaryAvvList["codice"] = i['codice']
            dictionaryAvvList["cliente"] = i['cliente']
            dictionaryAvvList["cate"] = i['cate']
            dictionaryAvvList["codcli"] = i['codcli']
            dictionaryAvvList["vornr"] = i['vornr']
            dictionaryAvvList["AUFPL"] = i['AUFPL']
            dictionaryAvvList["dipe"] = i['dipe']
            dictionaryAvvList["tempo"] = i['tempo']
            dictionaryAvvList["ARBID"] = i['ARBID']
            AvvList.append(dictionaryAvvList)    
    if AvvList == ap.ListaAvvitati:
        print("lista già aggiornata")
        return()
    else:
        list.clear(ap.ListaAvvitati)
        print(ap.ListaAvvitati)
        return(AvvList)


def premontaggi():
    cursor = conn.connessioneDatabase()
    query = "SELECT aufnr, matnr, maktx, dgltp, psmng, wemng, (psmng - wemng) AS resi, ntgew, fevor FROM vstdatin WHERE fevor = 'PRE';"
    query2 = "SELECT * FROM vstdatin"
    cursor.execute(query)
    ListaPremontaggi.clear()
    righe = cursor.fetchall()
    for i in righe:
        dictionaryPremontaggi = dict()
        dictionaryPremontaggi['aufnr'] = i[0]
        dictionaryPremontaggi['matnr'] = i[1]
        dictionaryPremontaggi['maktx'] = i[2]
        dictionaryPremontaggi['dgltp'] = i[3]
        dictionaryPremontaggi['psmng'] = i[4]
        dictionaryPremontaggi['resi'] = i[6]
        dictionaryPremontaggi['ntgew'] = i[7]
        ListaPremontaggi.append(dictionaryPremontaggi)
    if(ap.ListaPremontaggi != ListaPremontaggi):
        ap.ListaPremontaggi = list.copy(ListaPremontaggi)
    else:
        None

#funzione di estrapolazione dei dati dal database relativi all'ambiente di produzione "montaggio": IS2 AVV KTR XF

def datiMontaggio():
    cursor = conn.connessioneDatabase()
    query = "SELECT pwer, kdauf, kdpos, kunnr, name1, aufnr, matnr, maktx, dgltp, psmng, wemng, (psmng - wemng) AS resi, stato, fevor, atwrt1, atwrt, spedi,kdmat,ntgew,bismt,livello  FROM vstdatin WHERE fevor = 'IS2' OR fevor = 'KTR' OR fevor = 'XF' OR fevor = 'AVV';"
    cursor.execute(query)
    righe = cursor.fetchall()
    for i in righe:
        dictionaryListaMontaggio = dict()
        dictionaryListaMontaggio['pwer'] = i[0]
        dictionaryListaMontaggio['kdauf'] = i[1]
        dictionaryListaMontaggio['kdpos'] = i[2]
        dictionaryListaMontaggio['kunnr'] = i[3]
        dictionaryListaMontaggio['name1'] = i[4]
        dictionaryListaMontaggio['aufnr'] = i[5]
        dictionaryListaMontaggio['matnr'] = i[6]
        dictionaryListaMontaggio['maktx'] = i[7]
        dictionaryListaMontaggio['dgltp'] = i[8]
        dictionaryListaMontaggio['psmng'] = i[9]
        dictionaryListaMontaggio['wemng'] = i[10]
        dictionaryListaMontaggio['resi'] = i[11]
        dictionaryListaMontaggio['stato'] = i[12]
        dictionaryListaMontaggio['fevor'] = i[13]
        dictionaryListaMontaggio['atwrt1'] = i[14]
        dictionaryListaMontaggio['atwrt'] = i[15]
        dictionaryListaMontaggio['spedi'] = i[16]
        dictionaryListaMontaggio['kdmat'] = i[17]
        dictionaryListaMontaggio['ntgew'] = i[18]
        dictionaryListaMontaggio['bismt'] = i[19]
        dictionaryListaMontaggio['livello'] = i[20]
    if(ap.ListaMontaggio != ListaMontaggio):
        ap.ListaMontaggio = list.copy(ListaMontaggio)
    