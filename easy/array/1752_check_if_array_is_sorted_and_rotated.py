class Solution:
    def check(self, nums:list[int]) -> bool:
        count  = 0 
        n = len(nums) 
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                count += 1 

        return count <= 1

s = Solution()
print(s.check([3, 4, 5, 1, 2]))  
print(s.check([2, 1, 3, 4]))    
print(s.check([1, 2, 3]))      
print(s.check([1, 1, 1]))       
print(s.check([4, 5, 6, 7, 8, 1, 2, 3]))