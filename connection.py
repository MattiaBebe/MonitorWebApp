import pyodbc
import app as app
import app as ap

OrderList = [   
]
AstList = [
    
]

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