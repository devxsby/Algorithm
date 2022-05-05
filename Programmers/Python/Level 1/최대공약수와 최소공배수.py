# 최대공약수와 최소공배수
import math

def solution(n, m):
    answer = [math.gcd(n,m), n*m/math.gcd(n,m)]
    return answer

# 다른 풀이
'''
def gcdlcm(n, m):
    c, d = max(n, m), min(n, m)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(n*m/c)]
 
    return answer
'''