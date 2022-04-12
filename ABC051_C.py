from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="051"
#問題
problem="c"

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
  sx,sy,tx,ty=map(int,input().split())
  ans=[]
  for i in range(ty-sy):
    ans.append('U')
  for i in range(tx-sx):
    ans.append('R')
  for i in range(ty-sy):
    ans.append('D')
  for i in range(tx-sx):
    ans.append('L')
  ans.append('L')
  for i in range(ty-sy+1):
    ans.append('U')
  for i in range(tx-sx+1):
    ans.append('R')
  ans.append('D')
  ans.append('R')
  for i in range(ty-sy+1):
    ans.append('D')
  for i in range(tx-sx+1):
    ans.append('L')
  ans.append('U')
  print(*ans,sep='')
  """ここから上にコードを記述"""

  print(test_case[__+1])