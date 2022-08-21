import io
import sys

_INPUT = """\
6
2 2
1 1 1 2 1 3
1 2
2 2
10 3
-1000000000 -1000000000 1000000000 1000000000 -1000000000 1000000000
-1000000000 -1000000000
1000000000 1000000000
-1000000000 1000000000
300 0
0 0 1 0 0 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353 
  N,M=map(int,input().split())
  A,B,C,D,E,F=map(int,input().split())
  ban=[tuple(map(int,input().split())) for _ in range(M)]
  ban=set(ban)
  dp=[0]*(301**3)
  dp[0]=1
  tmp=[0]*(301**3)
  for i in range(300):
    for j in range(300-i):
      for k in range(300-i-j):
        l,m=A*i+C*j+E*k,B*i+D*j+F*k
        if (l+A,m+B) not in ban: dp[(i+1)*(301**2)+j*301+k]=(dp[(i+1)*(301**2)+j*301+k]+dp[i*(301**2)+j*301+k])%mod
        if (l+C,m+D) not in ban: dp[i*(301**2)+(j+1)*301+k]=(dp[i*(301**2)+(j+1)*301+k]+dp[i*(301**2)+j*301+k])%mod
        if (l+E,m+F) not in ban: dp[i*(301**2)+j*301+k+1]=(dp[i*(301**2)+j*301+k+1]+dp[i*(301**2)+j*301+k])%mod
  print(sum([dp[i*(301**2)+j*301+k] for i in range(301) for j in range(301) for k in range(301) if i+j+k==N])%mod)