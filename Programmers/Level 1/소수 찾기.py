# 소수 찾기
# 효율성 통과 못해서 다른 풀이 갖고 옴 
# 모범 답안 : 에라토스테네스의 체(Sieve of Eratosthenes)
def solution(n):
    answer = set(range(2,n+1))
    
    for i in range(2,n+1):
        if i in answer:
            answer -= set(range(i*2,n+1,i))
    return len(answer)