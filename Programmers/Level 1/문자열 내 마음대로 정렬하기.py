# 문자열 내 마음대로 정렬하기
def solution(strings, n):
    answer = []
    for i in strings:
        answer.append(i[n]+i)
    answer.sort()
    return [i[1:] for i in answer]

# 다른 풀이
'''
def solution(strings, n):
    return sorted(sorted(strings), key = lambda string:string[n])
'''