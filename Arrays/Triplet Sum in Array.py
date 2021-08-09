class Solution:
    def find3Numbers(self,A, n, X):
        for i in range(0, n-1):
            s= set()
            curr_sum = X - A[i]
            for j in range(i + 1, n):
                if (curr_sum - A[j]) in s:
                    return True
                s.add(A[j])
        return False

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,X=map(int,input().strip().split())
        A=list(map(int,input().strip().split()))
        ob=Solution()
        if(ob.find3Numbers(A,n,X)):
            print(1)
        else:
            print(0)
"""
Input:
n = 5, X = 10
arr[] = [1 2 4 3 6]
Output:
1
Explanation:
The triplet {1, 3, 6} in 
the array sums up to 10.
"""
