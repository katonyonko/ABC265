import io
import sys

_INPUT = """\
6
10 5 7 5
1 3 2 2 2 3 1 4 3 2
9 100 101 100
31 41 59 26 53 58 97 93 23
7 1 1 1
1 1 1 1 1 1 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,P,Q,R=map(int,input().split())
  A=list(map(int,input().split()))
  tmp=[[-1]*N for _ in range(3)]
  tmp2=[P,Q,R]
  ans='No'
  for i in range(3):
    t=0
    now=0
    for j in range(N):
      while now<N and t<tmp2[i]:
        t+=A[now]
        now+=1
      if t==tmp2[i]: tmp[i][j]=now-j
      t-=A[j]
  for i in range(N):
    if tmp[0][i]!=-1 and i+tmp[0][i]<N and tmp[1][i+tmp[0][i]]!=-1 and i+tmp[0][i]+tmp[1][i+tmp[0][i]]<N and tmp[2][i+tmp[0][i]+tmp[1][i+tmp[0][i]]]!=-1: ans='Yes'
  print(ans)