from typing import List

class Solution:
    def pivotIndex(self, nums):
        
        leftSum = 0
        rightSum = sum(nums) # sum of nums
        
        # i for index and ele for value.
        for i, ele in enumerate(nums):
            rightSum -= ele
            
            if leftSum == rightSum:
                return i
            else:
                leftSum += ele
        return -1

def main():
    sol = Solution()
    result = sol.pivotIndex([1,7,3,6,5,6]) # 28
    
    print(result)

if __name__ == "__main__":
    main()