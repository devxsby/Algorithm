# 문제 설명 :
# 골드바흐 수 :2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다.
# 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라 한다.
# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오.
# 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

''' 소수 구하기 (에라토스테네스의 체) '''
def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
'''골드바흐파티션 중 두 수의 차이가 작은 값 구하기'''
def goldPartition(n):
    result = [2] + list(range(3, (n//2)+1, 2))
    for i in reversed(result):
        if isPrime(i):
            if isPrime(n-i):
                return [i, n-i]

T = int(input()) # 테스트 케이스 입력

for _ in range(T):
    n = goldPartition(int(input()))
    for i in range(2):
        print(n[i], end =' ')