import sys
N, A, B = map(int, sys.stdin.readline().split(', '))
A, B, cnt = A-1, B-1, 0
while(A!=B):
    A, B = A//2, B//2
    cnt = cnt+1
print(cnt)