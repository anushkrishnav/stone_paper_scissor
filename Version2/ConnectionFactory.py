import pyodbc
def GetConnection():
    #conn_str=("driver={ODBC Driver 17 for SQL Server};Server='';Database='';user='';password='';")
    cxn=pyodbc.connect(driver='ODBC Driver 17 for SQL Server',server='', user='', password='', database='')
    return cxn
