import getpass
import pyodbc
from UInt import UserInterface
class LoginCK():
    def __init__(self):
        pass
    def signup(self):
        print("please fill the following\n")
        username=input("enter your user name :\t").lower()
        passw=getpass.getpass(prompt="set a password:\t").lower()
        conn_str=("driver={ODBC Driver 17 for SQL Server};Server='Anush';Database='gameDB';user='sa';password='Bu1ssnessman';")
        cxn=pyodbc.connect(driver='ODBC Driver 17 for SQL Server',server='Anush', user='sa', password='Bu1ssnessman', database='gameDB')
        cursor = cxn.cursor()
        cursor.execute('insert into user_details (Username,Password) VALUES(?,?)',username,passw)  
        cursor.commit()
        UserInterface.startGameNU(user_name)
        
    def login_Ck():
        username=input("enter your user name :\t").lower()
        passw=getpass.getpass(prompt="Your password:\t").lower()
        conn_str=("driver={ODBC Driver 17 for SQL Server};Server='Anush';Database='gameDB';user='sa';password='Bu1ssnessman';")
        cxn=pyodbc.connect(driver='ODBC Driver 17 for SQL Server',server='Anush', user='sa', password='Bu1ssnessman', database='gameDB')
        cursor = cxn.cursor()
        cursor.execute('SELECT Username,Password FROM user_details WHERE username= ? and password= ? ',username,passw)  
        cursor.commit()
