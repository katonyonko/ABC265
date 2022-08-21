import io
import sys

_INPUT = """\
6
2 3
RDU
LRU
2 3
RRD
ULL
9 44
RRDDDDRRRDDDRRRRRRDDDRDDDDRDDRDDDDDDRRDRRRRR
RRRDLRDRDLLLLRDRRLLLDDRDLLLRDDDLLLDRRLLLLLDD
DRDLRLDRDLRDRLDRLRDDLDDLRDRLDRLDDRLRRLRRRDRR
DDLRRDLDDLDDRLDDLDRDDRDDDDRLRRLRDDRRRLDRDRDD
RDLRRDLRDLLLLRRDLRDRRDRRRDLRDDLLLLDDDLLLLRDR
RDLLLLLRDLRDRLDDLDDRDRRDRLDRRRLDDDLDDDRDDLDR
RDLRRDLDDLRDRLRDLDDDLDDRLDRDRDLDRDLDDLRRDLRR
RDLDRRLDRLLLLDRDRLLLRDDLLLLLRDRLLLRRRRLLLDDR
RRRRDRDDRRRDDRDDDRRRDRDRDRDRRRRRRDDDRDDDDRRR
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  H,W=map(int,input().split())
  G=[input() for _ in range(H)]
  used=[[0]*W for _ in range(H)]
  now=(0,0)
  while True:
    i,j=now
    if G[i][j]=='U' and i>0: k,l=i-1,j
    elif G[i][j]=='D' and i<H-1: k,l=i+1,j
    elif G[i][j]=='L' and j>0: k,l=i,j-1
    elif G[i][j]=='R' and j<W-1: k,l=i,j+1
    else: ans=now; break
    if used[k][l]==1:
      ans=-1
      break
    else:
      now=(k,l)
      used[k][l]=1
  if ans==-1: print(ans)
  else: print(ans[0]+1,ans[1]+1)