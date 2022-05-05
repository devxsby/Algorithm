# 핸드폰 번호 가리기
def solution(phone_num):
    l = int(len(phone_num))
    answer = "*"*(l-4) + phone_num[l-4:]
    return answer