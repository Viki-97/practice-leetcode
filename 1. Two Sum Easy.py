from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.list_in=nums
        self.tgt=target
        self.list_out=[]
        for ind, list_val in enumerate(self.list_in):
            # print(ind, list_val, self.tgt-list_val)
            if self.tgt-list_val in self.list_in[ind+1:]:
                self.list_out.append(ind)
                self.list_out.append(self.list_in.index(self.tgt-list_val))
                break
        return self.list_out

s=Solution
s.twoSum(s,[3,2,4],6)