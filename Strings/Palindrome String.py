class Solution:
	def isPlaindrome(self, S):
        rev = ''.join(reversed(S))
        if (S == rev):
            return 1
        return 0

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPlaindrome(S)
		print(answer)
"""
Input: S = "abba"
Output: 1
Explanation: S is a palindrome
"""
