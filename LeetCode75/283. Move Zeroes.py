from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # a = find 0 stop
        # b =find non zero stop
        
        zero = 0
        # while a < b:
        #     if nums[a] == 0:
        #         nums[a] = nums[b]
        #         nums[b] = 0
        #         a += 1
        # print(nums)
        
        for nonZero in range(len(nums)):
            if nums[nonZero] != 0 and nums[zero] == 0:
                nums[zero], nums[nonZero] = nums[nonZero], nums[zero]
            if nums[zero] != 0:
                zero += 1
        
def main():
    sol = Solution()
    # result = sol.increasingTriplet([2,1,5,0,4,6])
    result = sol.moveZeroes([0,1,0,3,12])
    
    print(result)    


if __name__ == "__main__":
    main()
