class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()        
        words.reverse()
        answer = ' '.join(words)
        return answer
        

def main():
    sol = Solution()
    result = sol.reverseWords("the sky is blue")
    
if __name__ == "__main__":
    main()