# 수박수박수박수박수박수?
def solution(n):
    list = []
    for i in range (1,n+1):
        if i % 2 == 1:
            list.append('수')
        else:
            list.append('박')
    return ''.join(list)

# 다른 풀이 : 리스트 슬라이싱
'''
def water_melon(n):
    s = "수박" * n
    return s[:n]
'''