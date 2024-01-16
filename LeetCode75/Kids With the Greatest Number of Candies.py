from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        max_candy = max(candies)
        result = []
        for i in candies:
            if extraCandies + i >= max_candy:
                result.append(True)
            else:
                result.append(False)

        return result

def main():
    sol = Solution()
    result = sol.kidsWithCandies([2,3,5,1,3] , 3)
    print(result)
    
if __name__ == "__main__":
    main()