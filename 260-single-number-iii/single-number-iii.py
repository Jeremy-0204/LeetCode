class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = []
        rep = []
        for i in nums:
            if i not in x: x.append(i)
            else:
                if i not in rep: rep.append(i)

        return list(set(nums) - set(rep))