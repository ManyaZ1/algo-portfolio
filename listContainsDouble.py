class Solution(object):
    def containsDuplicate(self, nums):
        a=len(nums)
        b=len(set(nums))
        if(a!=b):
            return True;
        return False;

        """
        :type nums: List[int]
        :rtype: bool
        """
if __name__=="__main__":
    mylist=[1,2,3,3,4,5,6,7,8,9,0,8,6,4,13]
    p1=Solution()
    print(p1.containsDuplicate(mylist))
    #print("success")
        