from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        result = []
        current = "a"
        count = 0
        
        for c in chars:
            
            if current is c:
                count += 1
            else:
                
                current = c
                count = 0
                
                result.append(current)
                
            
        return result
        
def main():
    sol = Solution()
    result = sol.compress(["a","a","b","b","c","c","c"])
    print(result)
if __name__ == "__main__":
    main()