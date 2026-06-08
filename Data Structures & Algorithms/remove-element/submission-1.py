class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_index = 0
        for read_index in range(len(nums)):
            if nums[read_index] != val:
                #overwrite the element at the write index with the valid value
                nums[write_index] = nums[read_index]
                write_index += 1
        return write_index

        