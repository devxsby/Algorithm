# 6063 : [기초-3항연산] 정수 2개 입력받아 큰 값 출력하기(설명)(py)
a, b = input().split()
a = int(a)
b = int(b)
max = (a if (a>=b) else b) # 3항연산
print(int(max))