# 정수 내림차순으로 배치하기
def solution(n):
    lst = list(str(n))
    lst.sort(reverse = True)
    return int("".join(lst))