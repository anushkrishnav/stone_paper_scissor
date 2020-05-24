import pyodbc
def GetConnection():
    conn_str=("driver={ODBC Driver 17 for SQL Server};Server='{server name}';Database='{DB name}';user='';password='';")
    cxn=pyodbc.connect(driver='ODBC Driver 17 for SQL Server',server='', user='', password='', database='')
    return cxn