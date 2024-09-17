class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        nums.sort()
        length=len(nums)
        visited=set()
        sol=set()
        for i in range(length-2):
            if nums[i] in visited: continue
            visited.add(nums[i])
            target=0-nums[i]
            p1=i+1
            p2=length-1
            while (p1!=p2):
                s=nums[p1]+nums[p2]
                if s==target:
                    ls=(nums[p1],nums[p2])
                    if ls not in sol:
                        output.append([nums[i],nums[p1],nums[p2]])
                        sol.add( (nums[p1],nums[p2]))

                    p1+=1
                elif s>target:
                    p2-=1
                else:
                    p1+=1
        return output
#https://leetcode.com/problems/3sum/
            
