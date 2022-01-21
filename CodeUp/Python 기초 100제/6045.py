# 6045 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기(설명)(py)
a,b,c = map(int,input().split())
sum = a+b+c
print(sum, format((sum/3),".2f"))