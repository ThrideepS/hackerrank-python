if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True) 
    m1 = arr[0]
    m2 = arr[1]
    for i in range(n):
        if arr[i]==m1 and arr[i]==m2:
            m2 = arr[i+1]
    print(m2)
