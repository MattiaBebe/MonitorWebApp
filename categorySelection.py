from connection import AstList
import app as ap

AstList = []

def accessori(ListaOrdini):
    AstList.clear()
    print(AstList)
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
            AstList.append(dictionaryAstList)    
    if AstList == ap.ListaAste:
        print("lista già aggiornata")
    else:
        list.clear(ap.ListaAste)
        print(ap.ListaAste)
    return(AstList)


