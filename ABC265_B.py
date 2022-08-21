import io
import sys

_INPUT = """\
6
4 1 10
5 7 5
2 10
4 1 10
10 7 5
2 10
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M,T=map(int,input().split())
  A=list(map(int,input().split()))
  ans='Yes'
  d={}
  for _ in range(M):
    X,Y=map(int,input().split())
    d[X-1]=Y
  for i in range(N-1):
    T-=A[i]
    if T<=0:
      ans='No'
      break
    if i+1 in d: T+=d[i+1]
  print(ans)