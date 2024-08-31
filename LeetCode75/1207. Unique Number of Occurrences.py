from typing import List

# https://www.geeksforgeeks.org/sets-in-python/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1
        
        # set is not allowed duplicate
        print(freq.keys())
        print(freq)
        return len(freq) == len(set(freq.values()))
def main():
    sol = Solution()
    result = sol.uniqueOccurrences([1,2,2,2,3,3,3]) 
    
    print(result)

if __name__ == "__main__":
    main()