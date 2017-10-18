# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6
# Note:

# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.


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
