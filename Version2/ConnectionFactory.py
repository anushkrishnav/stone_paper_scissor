import pyodbc
def GetConnection():
    conn_str=("driver={ODBC Driver 17 for SQL Server};Server='Anush';Database='gameDB';user='sa';password='Bu1ssnessman';")
    cxn=pyodbc.connect(driver='ODBC Driver 17 for SQL Server',server='Anush', user='sa', password='Bu1ssnessman', database='gameDB')
    return cxn