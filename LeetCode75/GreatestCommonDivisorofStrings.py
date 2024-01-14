import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result = ""
        
        minLength = min(len(str1), len(str2))
        
        x = math.gcd(len(str1), len(str2))    

        if str1+str2 == str2+str1:
            for i in range(x):
                if str1[i] == str2[i]:
                    result += str1[i]
                else:
                    pass
            return result
        else:
            return ""
def main():
    sol = Solution()
    result = sol.gcdOfStrings("ABCDEF", "ABC")
    print(result)
    
if __name__ == "__main__":
    main()