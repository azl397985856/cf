t = int(input())
for _ in range(t):
    input()
    A = list(map(int, input().split(" ")))
    B = list(map(int, input().split(" ")))
    first = sum(A[1:])
    second = 0
    ans = float("inf")
    for i in range(len(A)):
        ans = min(ans, max(first, second))
        if i + 1 < len(A):
            first -= A[i + 1]
        second += B[i]
    print(ans)
