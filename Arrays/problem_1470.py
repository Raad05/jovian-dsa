class Solution:
    def shuffle(self, nums, n):
        arr = []
        for i in range(n):
            arr.append(nums[i])
            arr.append(nums[i + n])

        return arr