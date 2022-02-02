# 자연수 뒤집어 배열로 만들기
n = 3561
def solution(n):
    print list(map(int,reversed(str(n))))