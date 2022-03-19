N, M = map(int,input().split()) # N: 카드 개수, M: 합으로 넘지 않아야 하는 수
cardNumber = list(map(int,input().split()))
result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if cardNumber[i] + cardNumber[j] + cardNumber[k] > M:
                continue
            else:
                result = max(result, cardNumber[i] + cardNumber[j] + cardNumber[k])

print(result)