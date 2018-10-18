n = int(input())
l = sorted(int(input()) for _ in range(n))
print(
    min(l[i] - l[i-1] for i in range(1, n)),
)
