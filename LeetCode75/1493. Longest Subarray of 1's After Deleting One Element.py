from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = right = 0
        remove_chance = 1 
        result = 0
        # we need to find maximum right - left
        for right in range(len(nums)):
            
            if nums[right] == 0:
                # to point last zero index
                remove_chance -= 1

            while remove_chance < 0 and left <= right:
                if nums[right] == 0:
                    remove_chance +=1 
                left += 1
            result = max(result, right-left)
        return result
        #     if A[right] == 0:
        #         flip_chance -=1
        #     # case in 1100, flip_chance = 0, however 1 1 0 0 0 is k is less than 0, left is still 1 right is 0
            
        #     if flip_chance < 0:
        #         # if we already used flip chance, get back the chance
        #         if A[left] == 0:
        #             flip_chance += 1
        #         # moving to next
        #         left += 1
        
        # return right - left + 1
        
        #  [0,1,1,1,0,1,1,0,1]
        # 
        # 
        
def main():
    sol = Solution()
    result = sol.longestSubarray([0,1,1,1,0,1,1,0,1])    
    print(result)

if __name__ == "__main__":
    main()