class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = None, 0
        for n in nums:
            if count == 0:
                candidate = n 
            count += (1 if n == candidate else -1)
            print(count)
        
        return candidate