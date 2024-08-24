from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            # Add the current subset to the result
            result.append(path[:])
            
            # Explore further subsets
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                path.append(nums[i])
                # Recursively explore with nums[i] included
                backtrack(i + 1, path)
                # Exclude nums[i] from the current subset and move to the next
                path.pop()
        
        result = []
        backtrack(0, [])
        return result
