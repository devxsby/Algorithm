# 문제 설명 :
# 임의의 자연수 n보다 크고 2n보다 작은 소수의 개수를 출력 (입력 마지막 : 0)

''' 소수 구하기 (에라토스테네스의 체) '''
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
num_range = (range(2,246912))
result_list = []

for i in num_range:
    if isPrime(i):
        result_list.append(i)
        
while True:
    count = 0
    n = int(input())
    if n == 0:
        break

    for i in result_list:
        if n < i <= 2*n:
            count += 1
    print(count)