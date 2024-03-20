class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
                        
        i, j =  0, 0
        
        if len(s) != 0:

            while i < len(s) and j < len(t):
                
                if s[i] == t[j]:
                    i += 1
                j += 1
                if i == len(s):
                    return True
            return False
        else:
            return True
def main():
    sol = Solution()
    result = sol.isSubsequence("b", "abc")
    
    print(result)


if __name__ == "__main__":
    main()