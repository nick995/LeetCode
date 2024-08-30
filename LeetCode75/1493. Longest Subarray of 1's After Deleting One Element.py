from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        remove_chance = 1 
        result = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                remove_chance -= 1

            # in this case, we found 2 zeros, need to adjust left pointer
            if remove_chance < 0:
                # Move the left pointer to the right until we can remove one zero again
                while nums[left] != 0:
                    left += 1
                # Skip the zero at left
                left += 1
                # After removing that zero, restore the remove_chance
                remove_chance += 1

            result = max(result, right - left)
        
        return result
        
def main():
    sol = Solution()
    result = sol.longestSubarray([0,1,1,1,0,1,1,0,1])    
    print(result)

if __name__ == "__main__":
    main()