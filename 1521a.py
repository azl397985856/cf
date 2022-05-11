t = int(input())
for _ in range(t):
    a, b = map(int, input().split(" "))
    if b == 1:
        print("NO")
    else:
        print("YES")
        print(a * b, a, a * b + a)
