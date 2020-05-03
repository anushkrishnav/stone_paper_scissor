
import pyodbc
#print(conn_str)
#cxn=pyodbc.connect(conn_str)

def GetConnection():
    conn_str=("driver={ODBC Driver 17 for SQL Server};Server='Anush';Database='gameDB';user='sa';password='Bu1ssnessman';")
    cxn=pyodbc.connect(driver='ODBC Driver 17 for SQL Server',server='Anush', user='sa', password='Bu1ssnessman', database='gameDB')
    return cxn

conn=GetConnection()
cursor = conn.cursor()
cursor.execute()  
row = cursor.fetchone()  
while row:  
    print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
    row = cursor.fetchone()  
