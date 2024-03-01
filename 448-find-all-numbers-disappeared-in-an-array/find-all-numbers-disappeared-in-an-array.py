class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums2 = [i for i in range(1, len(nums) + 1)]
        return list(set(nums2) - set(nums))