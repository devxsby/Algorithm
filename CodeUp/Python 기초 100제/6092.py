# 6092 : [기초-리스트] 이상한 출석 번호 부르기1(설명)(py)
n = int(input())
list = input().split()
d = [] # 공백 리스트
    
for i in range(24):
    d.append(0)
    
for i in range(n):
    d[int(list[i])] += 1 # 번호 부를때마다 카운트 1씩 증가
    
for i in range(1,24):
    print(d[i], end=" ")