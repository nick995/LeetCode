from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        start_point = 0
        last_point = len(height)-1
        amount = 0
        answer = 0
        mxh = max(height)

        # requirement = largest number, fartest number
        # if find maximum number, start_point set up
        # if amount <  (last_point's index - start_point's index) * value of second_point
        #   amount update
         
        while start_point < last_point:
            
            amount = (last_point- start_point) * min(height[start_point], height[last_point])
            
            answer = max(answer, amount)
            if mxh * (last_point - start_point) <= answer:
                break
            
            if height[start_point] < height[last_point]:
                start_point +=1 
            else:
                last_point -= 1    
        return answer        
    
def main():
    sol = Solution()
    result = sol.maxArea([1,8,6,2,5,4,8,3,7]
)
    
if __name__ == "__main__":
    main()