# 6093 : [기초-리스트] 이상한 출석 번호 부르기2(py)
n = int(input())
listValue = input().split()
listValue.reverse()

for i in range(0,n):
    print(listValue[i], end=' ')