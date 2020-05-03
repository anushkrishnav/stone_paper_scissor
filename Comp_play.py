from termcolor import colored
#functions used if computer plays 
def com_stone(user,computerPlay,user_input):
    score=0
    if user_input=='paper':
        print("computer played",computerPlay)
        print(user,"gets a point")
        score=score+1
        
    else :
        print("computer played",computerPlay)
        print(user,colored("looses a point",'red'))
        score=score-1
    return score

def com_paper(user,computerPlay,user_input):
    score=0
    if user_input=='scicssor':
        print("computer played",computerPlay)
        print(user,"gets a point")
        score=score+1
    else :
        print("computer played",computerPlay)
        print(user,colored("looses a point",'red'))
        score=score-1
    return score

def com_scicssor(user,computerPlay,user_input):
    score=0
    if user_input=='stone':
        print("computer played",computerPlay)
        print(user,"gets a point")
        score=score+1
    else :
        print("computer played",computerPlay)
        print(user,colored("looses a point",'red'))
        score=score-1
    return score
