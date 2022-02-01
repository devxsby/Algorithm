# 문자열 내림차순으로 배치하기
# ''.join(리스트) 함수 : 리스트 요소 합쳐 하나의 문자열로 반환 
def solution(s):
    return ''.join(sorted(s,reverse = True))