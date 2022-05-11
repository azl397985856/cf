# t = int(input())
# for i in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     if max(a) == min(a):
#         print("NO")
#     else:
#         print("YES")
#         for j in range(len(a) - 1):
#             r = len(a) - 1
#             while a[j] == a[r]:
#                 r -= 1
#             print(j + 1, r + 1)
t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split(" ")))
    x = A[0]
    y = -1
    for i in range(1, n):
        if A[i] != A[0]:
            y = i
    if y == -1:
        print("NO")
    else:
        print("YES")
        # either assign x or y
        for i in range(1, n):
            if A[i] == x:
                print(i + 1, y + 1)
            else:
                print(i + 1, 1)
