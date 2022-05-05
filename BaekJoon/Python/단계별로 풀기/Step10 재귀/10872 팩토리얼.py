#for문을 사용한 팩토리얼 소스 코드 
n = int(input())
result = 1
for i in range (1, n+1, 1):
    result *= i
print(result)

# 재귀함수
'''
def factorial(n): 
    if(n > 1): 
        return n * factorial(n - 1) 
    else: 
        return 1 
    a = int(input()) 
    print(factorial(a))
    
n = int(input())
print(factorial(n))
'''