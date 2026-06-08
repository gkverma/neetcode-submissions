class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        current_count = 0
        max_count = 0
        for i in range(0, n):
            if (nums[i] == 1):
                current_count += 1
                max_count = max(current_count, max_count)
            else:               
                current_count = 0
        return max_count
      
        