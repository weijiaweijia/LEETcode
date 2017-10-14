ass Solution(object):
    def judgeCircle(self, moves):
        nL=0
        nR=0
        nU=0
        nD=0
        for char in moves:
            if (char=="L"):
                nL+=1
            if(char=="R"):
                nR+=1
            if(char=="U"):
                nU+=1
            if(char=="D"):
                nD+=1
        if(nL==nR and nU==nD):
            return True
        else:
            return False 
