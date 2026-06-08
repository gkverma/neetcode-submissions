class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # brute force approach
        # max_num = -1
        # for i in range(len(arr)-1):
        #     for j in range(i + 1, len(arr)):
        #             max_num = max(max_num, arr[j])
        #     arr[i] = max_num
        #     max_num = -1
        # arr[len(arr)-1]= -1
        # return arr    

        # Instead of looking to the right for every single element, 
        # what if we iterate backwards from the end of the array?If we start from the right, we can track the maximum element we've seen so far in a single pass. This brings the time complexity down to a blazing fast $O(n)$.

        max_from_right = -1

        for i in range((len(arr) - 1), -1, -1):
            current_val = arr[i]
            arr[i] = max_from_right
            
            max_from_right = max(max_from_right, current_val)

        return arr









        