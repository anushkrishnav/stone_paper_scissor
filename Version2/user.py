class User():
    def __init__(self,uN='',passw='',wn=0):
        self.Set_Username(uN)
        self.Set_Password(passw)
        self.Set_Wins(wn)
    def Get_Username(self):
        return self.userName
    def Set_Username(self,value):
        self.userName=value
    def Get_Wins(self):
        return self.Win
    def Set_Wins(self,value):
        self.Win=value
    def Get_Password(self):
        return self.password
    def Set_Password(self,value):
        self.password=value
    
        