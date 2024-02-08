# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_of_all = 1
        answer = []
        zero_case = 0
        for i in nums:
            if i != 0 :
                product_of_all *= i
            else:
                zero_case += 1
        if zero_case >= 2:
            return [0] * len(nums)

        
        #   case 1: if there's 0, others should be zero
        
        #   case 1.1: only one zero 

        #   case 1.2: more than one zeros
        
        for i in nums:
            if i != 0 and zero_case == 0:
                answer.append(product_of_all // i)
            else:
                if i == 0:                    
                    answer.append(product_of_all)
                else:
                    answer.append(0)
                
        return answer


def main():
    sol = Solution()
    result = sol.productExceptSelf([-1,1,0,-3,3])
    print(result)
    

if __name__ == "__main__":
    main()