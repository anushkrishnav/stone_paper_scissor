
from Wins import Win
from GameController import GameController
from termcolor import colored
class GameUI():
    def GameInterface(obj):
        winobj=Win()
        winobj.Set_Username(obj.Get_Username())
        print("\t\t\t\t Let the game begin\n You dare to challange the Supreme Computer in the game of \n Stone \n Paper \n Scissor \nhahaha lets see if you can Defeat me ")
        print("Rules: \n 1)You can break scissor with a stone \n 2) You can wrap a stone with paper and make it useless \n 3) You can use scissor and cut the paper into Bits \nIf Luck is with you ,You shall win")
        print (colored("Choose Stone\n ",'red'))
        print(colored("Choose Paper \n",'green'))    
        print(colored("Choose Scissor\n ",'blue'))
        userchoice=str(input("Your play ?")).lower()
        score=GameController.PlayGame(winobj,userchoice)
        winobj.Set_Wins(score[0])
        print("Computer played :"+str(score[1]))
        if score[0] == -1:
            print(colored("Lucks not in your side You Loose ",'red'))
        elif score[0] == 0:
            print("You think like a Computer its a draw")
        else:
            print("Its a mere streak of luck , You Won ")
        print("Your score is ",score[0])
        again=input("\n Do you dare to challange the Supreme again ?\n Press Y for yes or any key for no :\t").lower().strip()
        if again[0]=='y':
            GameUI.GameInterface(obj)
        else :
            print("Run You are no different than others ")
            print("\t\t\tH I G H S C O R E")
            highscore=GameController.GetTop5()
            for uname,upscore in highscore:
                print("\t\t |"+str(uname).ljust(10)+"\t\t",'{:03}'.format(upscore),"\t |")
            
        

    
     


        
        