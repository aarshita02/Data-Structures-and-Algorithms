# Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.

# 1st Approach : O(m+n) Space complexity

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return []
        
        m,n = len(matrix), len(matrix[0])
        
        zeroes_row = [False] * m
        zeroes_col = [False] * n
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeroes_row[row] = True
                    zeroes_col[col] = True
        
        for row in range(m):
            for col in range(n):
                if zeroes_row[row] or zeroes_col[col]:
                    matrix[row][col] = 0
                    

# 2nd Approach : O(1) Space Complexity

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return []
        
        m,n = len(matrix), len(matrix[0])
        rowZero = False
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row>0:
                        matrix[row][0] = 0
                    else:
                        rowZero = True
        
        for row in range(1,m):
            for col in range(1,n):
                if matrix[0][col] == 0 or matrix[row][0]==0:
                    matrix[row][col] = 0
        
        if matrix[0][0] == 0:
            for row in range(m):
                matrix[row][0] = 0
        
        if rowZero:
            for col in range(n):
                matrix[0][col] = 0
