from UInt import UserInterface
class user():
    def __init__(self,uN='',passw='',wn=0):
        self.Set_Username(uN)
        self.set_Password(passw)
        self.set_Wins(wn)
    def Get_Username(self):
        return self.username
    def Set_Username(self,value):
        self.userName=value
    def Get_Wins(self):
        return self.Win
    def set_Wins(self,value):
        self.Win=value
    def GetPassword(self):
        return self.password
    def SetPassword(self,value):
        self.Password=value
    
        