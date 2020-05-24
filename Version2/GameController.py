import random
from Version2.GameDAC import GameDAC
class GameController():
    def GetTop5():
        data=GameDAC.GetTop5()
        return data
    def com_stone(user,computerPlay,user_input):
        score=0
        if user_input=='paper':
            score+=1
            
        else :
            score-=1
        return score

    def com_paper(user,computerPlay,user_input):
        score=0
        if user_input=='scissor':
            score+=1
        else :
            score-=1
        return score

    def com_scicssor(user,computerPlay,user_input):
        score=0
        if user_input=='stone':
            score+=1
        else :
            score-=1
        return score
    def PlayGame(obj,User_inputs): 
        username=str(obj.Get_Username())
        score=0
        gElements=['stone','paper','scissor'] 
        computerPlays=random.choice(gElements)
        if computerPlays == User_inputs:
            score=0
        elif computerPlays=="stone":
            score+=GameController.com_stone(username, computerPlays, User_inputs)
        elif computerPlays=="paper":
            score+=GameController.com_paper(username, computerPlays, User_inputs)
        elif computerPlays=="scissor":
            score+=GameController.com_scicssor(username, computerPlays, User_inputs)
        oldscore=GameDAC.GetOldScore(username)
        updatedscore=oldscore+score
        obj.Set_Wins(updatedscore)
        GameDAC.UpdateScore(obj)
        return [score,computerPlays]