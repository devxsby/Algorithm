# 6067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기(설명)(py)
n = int(input())
if n<0:
    if n%2==0:
        print('A') # 음수이면서 짝수일때
    else:
        print('B') # 음수이면서 홀수일때
else:
    if n%2==0:
        print('C') # 양수이면서 짝수일때
    else:
        print('D') # 양수이면서 홀수일때