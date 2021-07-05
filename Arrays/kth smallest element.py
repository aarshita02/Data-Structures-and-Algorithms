#Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. 
#It is given that all array elements are distinct.

class Solution:
    def kthSmallest(self,arr, l, r, k):
        arr.sort()
        return(arr[k-1])

if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
