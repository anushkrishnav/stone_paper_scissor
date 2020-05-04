from user import User
from UserDAC import UserDAC
from GameInterface import GameUI
class UserControl():
    def SignUp(obj):
        name=obj.Get_Username()
        check=UserDAC.CheckUserAvailablity(name)
        if check== True:
            raise ValueError('User name taken. SomeOther name maybe ?')
        else: 
            UserDAC.SaveUser(obj)
            UserControl.SignIN(obj)
    def SignIN(obj):
        name=obj.Get_Username()
        passw=obj.Get_Password()
        if UserDAC.VerifyUser(obj)==True:
            GameUI.GameInterface(obj)
        


        

        
