# 하샤드 수
def solution(x):
    if x % sum(list(map(int,str(x)))) == 0:
        return True
    else:
        return False