class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        result = ""
        temp_min = min(len(word1), len(word2))
                
        for i in range(temp_min):
            result += word1[i] + word2[i]
        
        if len(word1) > len(word2):
            result += word1[temp_min:]
        else:
            result += word2[temp_min:]

        return result
    
def main():
    sol = Solution()
    result = sol.mergeAlternately("abcd", "pq")
    print(result)
    
if __name__ == "__main__":
    main()