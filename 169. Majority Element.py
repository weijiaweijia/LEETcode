class Solution(object):
    def majorityElement(self, nums):
        set1=set(nums)
        for el in set1:
            if(nums.count(el)>len(nums)/2):
                return el
