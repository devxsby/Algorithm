# 문자열 다루기 기본
# .isdigit() 함수 : 문자열이 '숫자'로만 이루어져있는지 확인
def solution(s):
    if (len(s) == 4 or len(s) == 6):
        if (s.isdigit()):
            return True
        else:
            return False
    else:
        return False