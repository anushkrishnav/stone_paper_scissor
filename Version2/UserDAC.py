
from ConnectionFactory import GetConnection
class UserDAC():
    def SaveUser(obj):
        conn=GetConnection()
        cursor = conn.cursor()
        passw=obj.Get_Password()
        name=obj.Get_Username()
        cursor.execute('insert into User_Details (Username,Password) VALUES(?,?)',name,passw)  
        cursor.commit()
        cursor.close()
    
    def CheckUserAvailablity(name):
        conn=GetConnection()
        cursor = conn.cursor()
        cursor.execute('SELECT Count(*) FROM user_details WHERE username= ?',name) 
        numofrec=cursor.fetchone()[0]
        if numofrec>0:
            return True
        else:
            return False
        cursor.close()

    def VerifyUser(obj):
        conn=GetConnection()
        cursor = conn.cursor()
        passw=obj.Get_Password()
        name=obj.Get_Username()
        cursor.execute('SELECT Count(*) FROM user_details WHERE username= ? and [Password]= ? ;',name,passw) 
        numofrec=cursor.fetchone()[0]
        if numofrec>0:
            return True
        else:
            return False
        cursor.close()