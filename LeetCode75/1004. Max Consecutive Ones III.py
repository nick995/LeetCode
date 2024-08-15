from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = self.maxLength(nums, k, 0)
        i = 0
        # for i in range(1, len(nums)- max_length):

        while i >= len(nums) - max_length:           
            temp = self.maxLength(nums, k, i)
            
            max_length = max(temp, max_length)
            
        
        return max_length
            
    def maxLength(self, nums: List[int], k: int, index: int) -> int:
        flip_count = k
        max_length = 0
        i = index
        #   initialize max_length
        while flip_count > 0:
            if nums[i] == 0:
                flip_count -= 1
                max_length += 1
            else:
                max_length += 1
            i += 1
        return max_length
def main():
    sol = Solution()
    result = sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)    
    print(result)

if __name__ == "__main__":
    main()