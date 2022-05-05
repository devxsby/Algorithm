#for문을 사용한 피보나치 소스 코드 
n = int(input())
fibonacci = [0, 1]
for i in range(2, n+1):
    num = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(num)
print(fibonacci[n])

# 재귀함수
'''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))
'''