# 피보나치 수
def solution(n):
    fibonacci = [0, 1]
    for i in range(2, n+1):
        num = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(num)
    return (fibonacci[n]) % 1234567