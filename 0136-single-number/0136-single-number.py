class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_count = {}
        for i in nums:
            try:
                nums_count[i] += 1
            except:
                nums_count[i] = 1
        for k, v in nums_count.items():
            if v == 1: return k
            