t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split(" "))
    A = ["a"] * n
    for i in range(1, b):
        A[i] = chr(ord(A[i - 1]) + 1)
    for i in range(a, n):
        A[i] = A[i - a]
    print("".join(A))
