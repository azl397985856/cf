t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    d = []
    for i in range(n - 1):
        if A[i] == A[i + 1]:
            d.append(i + 1)
    if len(d) <= 1:
        print(0)
    else:
        print(max(1, d[-1] - d[0] - 1))
