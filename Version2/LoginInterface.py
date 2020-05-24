import getpass
from UserController import UserControl
from user import User
import string
from termcolor import colored
class LoginUI():
    def login(self):
        print("-----------------------------------------------------------------------------------------------")
        print(colored("\t \t\t\tLOGIN\n\n",'green'))
        ck_new_user=str(input("New User ? (Y/n)\n ")).lower().strip()
        obj=User()
        while True:
            username=input("Username:\t").lower().strip()
            if len(username)>0:
                break
            else:
                print("NUll not accepted")
        while True :
            passw=getpass.getpass(prompt="set a password:\t").lower().strip()
            if len(username)>0:
                break
            else:
                print("NUll not accepted")
        obj.Set_Username(username)
        obj.Set_Password(passw)
        obj.Set_Wins(0)

        if ck_new_user[0]=='y':
            try :
                UserControl.SignUp(obj)
            except Exception as error:
                print('Caught this error: ' + repr(error))
                self.login()
        elif ck_new_user[0]=='n':
            UserControl.SignIN(obj)
        else:
            print(colored("     INVALID REPLY   \n",'red'))
            self.login()    
    
    #def startGameNU(self):
     #   print(" welcome"user.getUsername,"You need to pick any one of the followin")
      #  print("'stone','paper','scicssor'")
        

