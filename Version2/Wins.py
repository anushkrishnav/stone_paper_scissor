class Win():
    def __init__(self,uN='',wn=0):
        self.Set_Username(uN)
        self.Set_Wins(wn)
    def Get_Username(self):
        return self.userName
    def Set_Username(self,value):
        self.userName=value
    def Get_Wins(self):
        return self.userwin
    def Set_Wins(self,value):
        self.userwin=value
