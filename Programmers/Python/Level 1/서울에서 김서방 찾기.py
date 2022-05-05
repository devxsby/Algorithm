# 서울에서 김서방 찾기
def solution(seoul):
    for i in range (len(seoul)):
        if seoul[i] == "Kim":
            answer = '김서방은 {}에 있다'.format(i)
    return answer

# 다른 풀이
# def findKim(seoul):
#    return "김서방은 {}에 있다".format(seoul.index('Kim'))