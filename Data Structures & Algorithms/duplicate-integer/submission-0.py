class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Use hash set to efficiently keep track of values we have alreday seen
        seen = set()
        # we iterate through the array 
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
                