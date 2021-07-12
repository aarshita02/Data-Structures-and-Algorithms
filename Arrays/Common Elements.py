class Solution:
    def common_element(self,v1,v2):
        common = []
        final = []
        for i in range(len(v1)):
            common.append(v1[i])
          
        
        for j in range(len(v2)):
            if v2[j] in common:
                final.append(v2[j])
        final.sort()
        return final

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        v1=[int(x) for x in input().strip().split()]
        m=int(input())
        v2=[int(x) for x in input().strip().split()]
        ob=Solution()
        ans=ob.common_element(v1, v2);
        print(*ans)
        print()
        
"""
Input:
5
3 4 2 2 4
4
3 2 2 7

Output:
2 2 3

Explanation:
The first list is {3 4 2 2 4}, and the second list is {3 2 2 7}. 
The common elements in sorted order are {2 2 3}
"""
