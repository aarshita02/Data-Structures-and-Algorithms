class Solution:
	def find_median(self, v):
		v.sort()
		if len(v)%2 ==0:
		    num1= int(len(v)/2)
		    sum= v[num1-1] + v[num1]
		    median= sum/2
		    return int(median)
	    else:
	        num2= int((len(v)+1)/2)
	        median= v[num2-1]
	        return int(median)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
    
"""
Input: N = 5
arr[] = 90 100 78 89 67
Output: 89
Explanation: After sorting the array 
middle element is the median
"""
