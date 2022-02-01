# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = []
    for i in range(1,1001):
        if len(answer) < n:
            answer.append(x*i)
    return answer

# 다른 풀이 : 한줄로 써서 깔끔함
'''
def solution(x, n):
    return [i for i in range(x, x*n+1, x)]
'''