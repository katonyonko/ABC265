import io
import sys

_INPUT = """\
6
1 5
0
3
3 10
2 6 5
2 1 2
10 100
3 1 4 1 5 9 2 6 5 3
2 7 1 8 2 8 1 8 2 8
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  N,D=map(int,input().split())
  p=list(map(int,input().split()))
  q=list(map(int,input().split()))
  tmp=[abs(p[i]-q[i]) for i in range(N)]
  