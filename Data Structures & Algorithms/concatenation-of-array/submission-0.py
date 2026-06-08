class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # ans = []
        # ans = [0] * 2 * n
        # for i in range(0, n):
        #     ans[i] = nums[i]
        #     ans[i + n] = nums [i]

        # for i in range (n, 2*n):
        #     ans[i] = nums[i-n]
    
        return nums + nums
