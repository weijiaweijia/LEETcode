class Solution(object):
    def firstUniqChar(self, s):
        lists=list(s)
        sets=set(lists)
        uniquelist=[]
        min=10000000000000
        for i in sets:
            if(lists.count(i)==1):
                uniquelist.append(i)
        if (len(uniquelist)==0):
            return -1
        for e in uniquelist:
            if(lists.index(e)<min):
                min=lists.index(e)
        return min
                
