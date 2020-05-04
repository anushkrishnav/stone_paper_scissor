from ConnectionFactory import GetConnection
class GameDAC():
    def GetOldScore(username):
        conn=GetConnection()
        cursor = conn.cursor()
        cursor.execute('SELECT TotalWins FROM user_details WHERE Username= ? ',username) 
        OldWins=cursor.fetchone()[0]
        cursor.close()
        if OldWins==None:
            OldWins=0
        return OldWins
        

    def UpdateScore(obj):
        conn=GetConnection()
        cursor = conn.cursor()
        score=obj.Get_Wins()
        name=obj.Get_Username()
        cursor.execute('Update User_Details set TotalWins= ? where Username= ?',score,name)  
        cursor.commit()
        cursor.close()
    
    def GetTop5():
        conn=GetConnection()
        cursor = conn.cursor()
        cursor.execute('Select top 5 Username,TotalWins from User_Details ORDER by TotalWins desc;') 
        WinersData=cursor.fetchall()
        cursor.close()
        return WinersData
