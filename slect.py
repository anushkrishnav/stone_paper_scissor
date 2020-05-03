import pyodbc
import getpass
def GetConnection():
    conn_str=("driver={ODBC Driver 17 for SQL Server};Server='Anush';Database='gameDB';user='sa';password='Bu1ssnessman';")
    cxn=pyodbc.connect(driver='ODBC Driver 17 for SQL Server',server='Anush', user='sa', password='Bu1ssnessman', database='gameDB')
    return cxn
username='asc' #input("enter your user name :\t").lower()
passw='asd'#getpass.getpass(prompt="Your password:\t").lower()
#conn_str=("driver={ODBC Driver 17 for SQL Server};Server='Anush';Database='gameDB';user='sa';password='Bu1ssnessman';")
#cxn=pyodbc.connect(driver='ODBC Driver 17 for SQL Server',server='Anush', user='sa', password='Bu1ssnessman', database='gameDB')
conn=GetConnection()
cursor = conn.cursor()
cursor.execute('SELECT Count(*) FROM user_details WHERE username= ? and password= ? ',username,passw) 
numofrec=cursor.fetchone()[0]
print(numofrec)
#print(len(cursor.fetchone()))
if numofrec>0:
    print("True")
else:
   print("Invalid")
cursor.close()