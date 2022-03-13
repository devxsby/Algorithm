''' 소수 구하기 (에라토스테네스의 체) '''
def isPrime(num):
    if num == 1:                              # 1은 모든 수의 약수이기 때문에 false
        return False
    else:
        for i in range(2, int(num**0.5) + 1): # 제곱근 있는 수 중에
            if num % i == 0:                  # 약수가 있으면 false
                return False
        return True                           # 이외는 소수(true)
    
# 사용 예시
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
PrimeNumber = []
for i in num:
    if isPrime(i) == True:
        PrimeNumber.append(i)
        
if len(PrimeNumber) > 0 :
    print(PrimeNumber)
    