import io
import sys

_INPUT = """\
6
10 25 10
10 40 10
100 100 2
100 100 100
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  X,Y,N=map(int,input().split())
  ans=10**100
  for i in range(N//3+1):
    ans=min(ans,i*Y+(N-3*i)*X)
  print(ans)