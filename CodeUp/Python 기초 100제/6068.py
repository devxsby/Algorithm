# 6068 : [기초-조건/선택실행구조] 점수 입력받아 평가 출력하기(설명)(py)
n = int(input())
if n >= 90:
    print('A')
elif n >= 70:
    print('B')
elif n >= 40:
    print('C')
else:
    print('D')