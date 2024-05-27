from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # initialize currSum and maxSum
        currSum = maxSum = sum(nums[:k])
        numLen = len(nums)
        
        #   until lengh of nums, add nums[i] and subtract nums[i-k] to find a maxSum
        for i in range(k, numLen):
            currSum += nums[i] - nums[i-k]
            
            if currSum > maxSum:
                maxSum = currSum
                
        return maxSum / k
def main():
    sol = Solution()
    result = sol.findMaxAverage([4,0,4,3,3], 5)
    
    print(result)

if __name__ == "__main__":
    main()