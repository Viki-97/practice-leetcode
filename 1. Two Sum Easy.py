from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         self.list_in=nums
#         self.tgt=target
#         self.list_out=[]
#         for ind, list_val in enumerate(self.list_in):
#             print(ind, list_val, self.tgt-list_val)
#             if self.tgt-list_val in self.list_in[ind+1:]:
#                 self.list_out.append(ind)
#                 self.list_out.append(self.list_in[ind+1:].index(self.tgt-list_val)+ind+1)
#                 break
#         return self.list_out

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index={} # creating dict to track nums as keys and index as values
        for ind, list_val in enumerate(nums):
            if target - list_val in num_to_index:
                return [num_to_index[target-list_val], ind]
            num_to_index[list_val]=ind
        
s=Solution
print(s.twoSum(s,nums = [2,7,11,15], target = 9))
print(s.twoSum(s,nums = [3,2,4], target = 6))
print(s.twoSum(s,[3,3],6))