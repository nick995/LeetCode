from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        # since starting altitude is 0
        altitude = 0
        result = 0
        for x in range(len(gain)):
            altitude += gain[x]
            result = max(result, altitude)
        return result
    
def main():
    sol = Solution()
    result = sol.largestAltitude([-5,1,5,0,-7])
    print(result)
if __name__ == "__main__":
    main()