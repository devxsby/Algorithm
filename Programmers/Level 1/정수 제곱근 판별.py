# 정수 제곱근 판별
def solution(n):
    if n**(1/2) == int (n**(1/2)):
        answer = (n**(1/2)+1)**2
    else:
        answer = -1
    return answer


# 다른 풀이 : 더 깔끔함. import math도 안해도 됨.
'''
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'
'''