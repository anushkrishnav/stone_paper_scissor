import random
from termcolor import colored
from Comp_play import com_paper,com_scicssor,com_stone

class main():
    def __init__(self):
        pass

def rand_gen():
    #gElement is an enum
    gElements=['stone','paper','scicssor'] 
    return random.choice(gElements)
def scoringCheck(User_inputs,user):
    computerPlays= rand_gen()
    if computerPlays == User_inputs:
        print ("computer played",computerPlays,"its a draw")
    elif computerPlays=="stone":
        score=score+com_stone(user,computerPlays,User_inputs)
    elif computerPlays=="paper":
        score=score+com_paper(user,computerPlays,User_inputs)
    elif computerPlays=="scicssor":
        score=score+com_scicssor(user,computerPlays,User_inputs)    
    updateScore()

def updateScore():
    pass


