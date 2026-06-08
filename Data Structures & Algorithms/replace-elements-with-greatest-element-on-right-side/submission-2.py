class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # brute force approach
        max_num = -1
        for i in range(len(arr)-1):
            for j in range(i + 1, len(arr)):
                    max_num = max(max_num, arr[j])
            arr[i] = max_num
            max_num = -1
        arr[len(arr)-1]= -1
        return arr    
        