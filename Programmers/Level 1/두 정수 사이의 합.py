# 두 정수 사이의 합
def solution(a, b):
    if a < b :
        return sum(list(range(a, b+1)))
    else:
        return sum(list(range(b, a+1)))