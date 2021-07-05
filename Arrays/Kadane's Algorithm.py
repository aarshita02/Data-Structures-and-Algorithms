"""Input:
N = 5
arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is equal to 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray."""

class Solution:
    def maxSubArraySum(self,a,size):
        max_so_far =a[0]
        curr_max = a[0]
     
        for i in range(1,size):
            curr_max = max(a[i], curr_max + a[i])
            max_so_far = max(max_so_far,curr_max)
         
        return max_so_far

import math 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
