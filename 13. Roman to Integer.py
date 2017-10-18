#Given a roman numeral, convert it to an integer.
#Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def romanToInt(self, s):
        d={'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        result=0
        for i in range(0,len(s)-1):
            if(d[s[i]]<d[s[i+1]]):
                result-=d[s[i]]
            else:
                result+=d[s[i]]
        result+=d[s[-1:]]
        return result
        
                
                 

        
        
