# while 문으로 돌렸다 시간초과 나와서 최대한 간단하게 표현함
a, b, v = map(int, input().split())
day = 1
if (v - a) % (a - b) == 0:
    day += int((v - a) / (a - b))
else:
    day += int((v - a) / (a - b) + 1)
print(day)