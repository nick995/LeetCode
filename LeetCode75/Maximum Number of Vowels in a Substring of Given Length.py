from typing import List
    
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]

        # Count vowels in the initial window
        maxVowel = currVowel = sum(s[i] in vowels for i in range(k))
        
        if maxVowel is k:
            return maxVowel
        else:
                    
            for i in range(k, len(s)):
                if s[i] in vowels:
                    currVowel +=1 
                if s[i-k+1] in vowels:
                    currVowel -= 1

                if currVowel > maxVowel:
                    maxVowel = currVowel
            return maxVowel
        
def main():
    sol = Solution()
    result = sol.maxVowels("tryhard", 4)
    
    print(result)

if __name__ == "__main__":
    main()