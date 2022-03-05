# 부족한 금액 계산하기
def solution(price, money, count):
    result = 0
    for i in range(1,count+1):
        result += price * i
    if result >= money:
        answer = result -money
    else:
        answer = 0
    return answer