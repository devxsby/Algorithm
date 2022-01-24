# 6064 : [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기(설명)(py)
a, b, c = map(int,input().split())
min = (a if a<b else b) if ((a if a<b else b)<c) else c # 3항연산 
print(int(min))