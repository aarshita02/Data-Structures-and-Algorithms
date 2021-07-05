# Defining a reverse function
 def reverselist (A, start, end):
    while start< end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
        
#Demo array    
A = [1,2,3,4,5,6,7,8]
print(A)
reverselist(A,0,7)
print(A)
