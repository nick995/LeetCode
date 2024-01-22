class Solution:
    def reverseVowels(self, s: str) -> str:

        start = 0
        last = len(s)
        vowels = "aeiouAEIOU"
        check_point = 0
        temp = ''
        words = list(s)
        while start < last:
            if words[start] in vowels:
                check_point = start
                temp = words[start]
                while last >= check_point:
                    last -= 1
                    if words[last] in vowels:
                        
                        words[check_point] = words[last]
                        words[last] = temp
                        start +=1
                        break
            else:
                start += 1
        
        return ''.join(words)
        

def main():
    sol = Solution()
    result = sol.reverseVowels(" ")
    print(result)
    


if __name__ == "__main__":
    main()