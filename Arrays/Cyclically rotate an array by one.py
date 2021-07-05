def rotate( arr, n):
    i=0
    j=n-1
    while i!=j:
        arr[i], arr[j]= arr[j], arr[i]
        i +=1

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()

# Input = [1,2,3,4,5]
# Output = [5,1,2,3,4]
