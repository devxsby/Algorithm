# 소수 찾기
def solution(n):
    count = 0
    for n in range(2, n+1):
        for i in range(2, n):
            if n%i == 0: # 소수 아님
                break
        else:    
            count += 1
    return count

# 다른 풀이 : 에라토스테네스의 체(Sieve of Eratosthenes)
'''
def solution(n):
    num = set(range(2,n+1))
    
    for i in range(2,n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
 
    return len(num)
'''