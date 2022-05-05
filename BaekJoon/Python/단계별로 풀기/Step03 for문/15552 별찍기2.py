import sys #sys모듈 읽어오기
case = int(input())
for i in range(case):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)