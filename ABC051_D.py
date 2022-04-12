from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="051"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/abc{0}_{1}".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  def WF(cost):
    for k in range(len(cost)):
        for i in range(len(cost)):
            for j in range(len(cost)):
                if cost[i][k]!=INF and cost[k][j]!=INF:
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    return cost
  N,M=map(int,input().split())
  INF=10**6
  cost=[[INF]*N for i in range(N)]
  edge=[]
  ans=0
  for i in range(M):
    a,b,c=map(int,input().split())
    a-=1; b-=1
    cost[a][b]=c
    cost[b][a]=c
    edge.append((a,b,c))
  WF(cost)
  for i in range(M):
    a,b,c=edge[i]
    if cost[a][b]!=c: ans+=1
  print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])