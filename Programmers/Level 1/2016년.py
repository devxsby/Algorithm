# 2016년
def solution(a, b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    return days[(sum(months[:a-1])+b)%7]

# 다른 풀이 : datetime 라이브러리 사용
'''
import datetime

def solution(a, b):
    answer = ''
    days =['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    answer = days[datetime.date(2016, a, b).weekday()]
    return answer

'''