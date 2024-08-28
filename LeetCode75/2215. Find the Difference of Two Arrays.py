from typing import List

# https://www.geeksforgeeks.org/sets-in-python/

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Convert lists to sets to find unique elements
        num_set1, num_set2 = set(nums1), set(nums2)

        # Find elements unique to each set
        unique1 = list(num_set1 - num_set2)
        unique2 = list(num_set2 - num_set1)
        
        # Return the unique elements as a list of lists
        return [unique1, unique2]
def main():
    sol = Solution()
    result = sol.findDifference([1,2,3], [2,4,6]) # 28
    
    print(result)

if __name__ == "__main__":
    main()