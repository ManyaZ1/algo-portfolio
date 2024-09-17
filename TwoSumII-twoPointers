class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p2=len(numbers)-1
        p1=0
        while True:
            s=numbers[p1]+numbers[p2]
            if s==target:
                output=[p1+1,p2+1]
                return output
            elif s>target:
                p2-=1
            else:
                p1+=1

