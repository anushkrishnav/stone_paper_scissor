
from signup_login import LoginCK 
from user import user
#from userFactory import userFactory
import string
import termcolor
from termcolor import colored
from main import main
class UserInterface():
    def __init__(self):
        pass
    print("-----------------------------------------------------------------------------------------------")
    print(colored("\t \t\t\tWelcome\n\n",'green'))
    def login(self):
        ck_new_user=str(input("Exsisting user ? (Y/n)\n ")).lower().strip()
        if ck_new_user[0]=='y':
            LoginCK.login_Ck()
            #user details  validation
            if LoginCK.login_Ck==True:
                UserInterface.startGameNU()
        elif ck_new_user[0]=='n':
            LoginCK.signup()
        else:
            print(colored("     INVALID REPLY   \n",'red'))
            UserInterface.login()    
    def startGameNU(self):
        print(" welcome"user.getUsername,"You need to pick any one of the followin")
        print("'stone','paper','scicssor'")
        
        main.scoringCheck(playerPlay,user.getUsername)

