from collections import deque

d = deque()
N = int(input())

for _ in range(N):
    comm, *num = input().split()
    eval(f"d.{comm}({str(*num)})")

print(*d)