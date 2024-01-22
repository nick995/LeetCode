from typing import List

class Solution:
    
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        prev_changed = False        
        temp_n = n
        
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n == 1:
                temp_n -=1        
        for i in range(0,len(flowerbed)-1):
            if flowerbed[i] ==0:
                print(i)
                if i == 0 or i == (len(flowerbed)-2):
                    if flowerbed[i+1] != 1 or None:
                        temp_n -= 1
                        prev_changed = True
                else:                
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and prev_changed == False:
                        temp_n -=1
                        prev_changed = True
                    else:
                        prev_changed = False

        if temp_n == 0:
            return True
        else:
            return False
def main():
    sol = Solution()
    result = sol.canPlaceFlowers([1,0,0,0,1]

, 1)
    print(result)
    
if __name__ == "__main__":
    main()