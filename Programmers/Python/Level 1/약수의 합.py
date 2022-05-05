# 약수의 합
def solution(n):
    list = []
    for i in range(1, n+1):
        if n % i == 0:
            list.append(i)
    return sum(list)