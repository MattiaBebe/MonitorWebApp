import pyodbc
import app as app
import app as ap

OrderList = [   
]
AstList = [
    
]
ListaDati = []

def connessioneDatabase():
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=192.168.1.54\SQLEXPRESS;'
                        'Database=cypag_dev;'
                        'UID=Mattia;'
                        'PWD=&Mattbert89;'
                        'Trusted_Connection=yes;')

    cursor = conn.cursor()

    return(cursor)

def estrazioneOridini():
    cursor = connessioneDatabase()
    cursor.execute('SELECT top(100) * FROM tblscarico')
    righe = cursor.fetchall()
    if ap.righeTMP != righe:
        ap.righeTMP = righe
        for i in righe:
            dictionaryOrderList = {
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
            dictionaryOrderList["chiave"] = i[0]
            dictionaryOrderList["ordine"] = i[1]
            dictionaryOrderList["qta"] = i[2]
            dictionaryOrderList["cance"] = i[3]
            dictionaryOrderList["errore"] = i[4]
            dictionaryOrderList["data"] = i[5]
            dictionaryOrderList["codice"] = i[6]
            dictionaryOrderList["cliente"] = i[7]
            dictionaryOrderList["cate"] = i[8]
            dictionaryOrderList["codcli"] = i[9]
            dictionaryOrderList["vornr"] = i[10]
            dictionaryOrderList["AUFPL"] = i[11]
            dictionaryOrderList["dipe"] = i[12]
            dictionaryOrderList["tempo"] = i[13]
            dictionaryOrderList["ARBID"] = i[14]
            OrderList.append(dictionaryOrderList)
            ap.ListaOrdini = list.copy(OrderList)
    return(OrderList)

def estrazioneDati():
    cursor = connessioneDatabase()
    cursor.execute('SELECT * FROM tbldati')
    righe = cursor.fetchall()
    for i in righe:
            dictionaryDateList = {
                                    "PWER" : None,
                                    "KDAUF" : None,
                                    "KDPOS" : None,
                                    "KUNNR" : None,
                                    "name1" : None,
                                    "aufnr" : None,
                                    "matnr" : None,
                                    "maktx" : None,
                                    "dgltp" : None,
                                    "psmng" : None,
                                    "wemng" : None,
                                    "fevor" : None,
                                    "stato" : None,
                                    "atwrt1" : None,
                                    "atwrt" : None,
                                    "spedi" : None,
                                    "kdmat" : None,
                                    "klabc" : None,
                                    "ntgew" : None,
                                    "stlbez" : None,
                                    "bismt" : None,
                                    "linea" : None,
                                    "aufpl" : None
                                }
            dictionaryDateList["PWER"] = i[0]
            dictionaryDateList["KDAUF"] = i[1]
            dictionaryDateList["KDPOS"] = i[2]
            dictionaryDateList["KUNNR"] = i[3]
            dictionaryDateList["name1"] = i[4]
            dictionaryDateList["aufnr"] = i[5]
            dictionaryDateList["matnr"] = i[6]
            dictionaryDateList["maktx"] = i[7]
            dictionaryDateList["dgltp"] = i[8]
            dictionaryDateList["psmng"] = i[9]
            dictionaryDateList["wemng"] = i[10]
            dictionaryDateList["fevor"] = i[11]
            dictionaryDateList["stato"] = i[12]
            dictionaryDateList["atwrt1"] = i[13]
            dictionaryDateList["atwrt"] = i[14]
            dictionaryDateList["spedi"] = i[15]
            dictionaryDateList["kdmat"] = i[16]
            dictionaryDateList["klabc"] = i[17]
            dictionaryDateList["ntgew"] = i[18]
            dictionaryDateList["stlbez"] = i[19]
            dictionaryDateList["bismt"] = i[20]
            dictionaryDateList["linea"] = i[21]
            dictionaryDateList["aufpl"] = i[22]
            ListaDati.append(dictionaryDateList)
    return(ListaDati)