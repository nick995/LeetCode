from typing import List

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = right = 0
        flip_chance = K 
        # we need to find maximum right - left
        for right in range(len(A)):
            
            if A[right] == 0:
                flip_chance -=1
            # case in 1100, flip_chance = 0, however 1 1 0 0 0 is k is less than 0, left is still 1 right is 0
            
            if flip_chance < 0:
                # if we already used flip chance, get back the chance
                if A[left] == 0:
                    flip_chance += 1
                # moving to next
                left += 1
        
        return right - left + 1
        
def main():
    sol = Solution()
    result = sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)    
    print(result)

if __name__ == "__main__":
    main()