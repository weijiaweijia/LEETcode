class Solution(object):
    def findShortestSubArray(self, nums):
            if (len(nums)==1):
                return 1
            set1 = set(nums)
            list1 = []
            max1 = 0
            if(len(set1)==len(nums)):
                return 1
            for el in set1:
                c = nums.count(el)
                list1.append(c)
                if (c > max1):
                    max1 = nums.count(el)
            degree=[]
            for elment in set1:
                if (nums.count(elment)==max1):
                    degree.append(elment)
            minindexd=[]
            for eachdeg in degree:
                inte = 0
                index = []
                index1=nums.index(eachdeg)
                index2=len(nums) - nums[::-1].index(eachdeg) - 1
                newlist = nums[index1:index2]
                minindexd.append(len(newlist)+1)
            return min(minindexd)
