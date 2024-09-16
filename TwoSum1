from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict=defaultdict(lambda: "Not Present")
        pos=-1
        for element in nums:
            pos+=1
            missing=target-element
        # print(f"pos:{pos}  missing:{missing}")
            if(dict[missing]=="Not Present"):
                dict[element]=pos
                #print(dict)
            else:
                output=[dict[missing],pos]
                return output
#https://leetcode.com/problems/two-sum/description/
