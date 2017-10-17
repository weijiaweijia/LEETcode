# Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

# Example 1:
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
# For the left two athletes, you just need to output their relative ranks according to their scores.
# Note:
# N is a positive integer and won't exceed 10,000.
# All the scores of athletes are guaranteed to be unique.

class Solution(object):
    def findRelativeRanks(self, nums):
        if(len(nums)==1):
            return ["Gold Medal"]
        elif(len(nums)==2):
            if(nums[0]<nums[1]):
                return ["Silver Medal","Gold Medal"]
            else:
                return ["Gold Medal","Silver Medal"]
        else:
            seq = sorted(nums,key=int,reverse=True)
            index1 = [str(seq.index(v)+1) for v in nums]
            index1[index1.index("1")]="Gold Medal"
            index1[index1.index("2")]="Silver Medal"
            index1[index1.index("3")]="Bronze Medal"
            return index1

#         temp = []
#         for n in nums:
#             temp.append(n)
#         nums = sorted(nums, key=int, reverse=True)
        
        # for e in temp:
        #     if(nums.index(e)==0):
        #         temp[temp.index(e)] = "Gold Medal"
        #     elif(nums.index(e)==1):
        #         temp[temp.index(e)] = "Silver Medal"
        #     elif(nums.index(e)==2):
        #         temp[temp.index(e)] = "Bronze Medal"
        #     else:
        #         temp[temp.index(e)]=str(nums.index(e)+1)
        # return temp
