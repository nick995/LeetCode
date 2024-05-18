from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        temp = {}
        answer = 0
        # initialize
        for x in nums:
            if x in temp:
                temp[x] += 1
            else:
                temp[x] = 1
        target = 0
        for x in temp:
            target = k - x
            
            if x> target:
                pass
            else:
                if x == target:
                    answer += temp[x]/2
                    
                else:    
                    if target in temp:
                        answer += min(temp[x], temp[target])
        return int(answer)
def main():
    sol = Solution()
    result = sol.maxOperations([5000000, 5000000, 5000000, 5000000], 10000000)
    print(result)
    

if __name__ == "__main__":
    main()