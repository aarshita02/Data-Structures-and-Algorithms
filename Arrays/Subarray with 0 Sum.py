"""
Input:
5
4 2 -3 1 6

Output: 
Yes

Explanation: 
2, -3, 1 is the subarray 
with sum 0.
"""
class Solution:
    def subArrayExists(self,arr,n):
        n_sum = 0
        s = set()

        for i in range(n):
            n_sum += arr[i]
            if n_sum == 0 or n_sum in s:
                return True
            s.add(n_sum)

        return False

def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
