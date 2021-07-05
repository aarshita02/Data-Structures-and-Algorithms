#Sorting arrays without using the sort function

class Solution:
    def sort012(self,arr,n):
        count0 = 0
        count1= 0
        count2 =0
        for i in range(0, n):
            if arr[i]==0:
                count0 += 1
            if arr[i]==1:
                count1 += 1
            if arr[i]==2:
                count2 += 1
        
        for i in range(0, count0):
            arr[i]=0
        for i in range(count0, count0+ count1):
            arr[i] =1
        for i in range (count0 + count1,n):
            arr[i]=2
        return(arr)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()
