from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        print(nums)
        smallest = second_small = 99999999999
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= second_small:
                second_small = num
            else:
                return True
        return False
                
                
            
    
def main():
    sol = Solution()
    result = sol.increasingTriplet([2,1,5,0,4,6]
)
    
    print(result)
    


if __name__ == "__main__":
    main()