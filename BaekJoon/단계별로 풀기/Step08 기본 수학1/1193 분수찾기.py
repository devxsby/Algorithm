# 모범 답안
x = int(input())
line = 0 # 사선 라인
num_count = 0 # 입력값 x의 라인에서 가장 큰 숫자

while num_count < x:
    line += 1
    num_count += line
    
num_count -= line

if line % 2 == 0: # 사선 라인이 짝수번째 일때
    i = x - num_count # 분자
    j = line - i + 1 # 분모
else: # 사선 라인이 홀수번째 일 때
    i = line - (x - num_count) + 1 # 분자
    j = x - num_count # 분모

print(f"{i}/{j}")

# 첫번째 풀이 : 메모리 초과
'''
x = int(input())
            # x =   1  2 3  4 5 6  7 8 9 10  11 12 13 14 15
            # i =   1   2     3       4            5
a = [] # 분자 : 1  1 2  3 2 1  1 2 3 4   5  4  3  2  1 
b = [] # 분모 : 1  2 1  1 2 3  4 3 2 1   1  2  3  4  5

for i in range (1, int(x)): 
    if i % 2 == 1: # i 홀수 : 분자 역방향, 분모 정방향
        for j in range (1, i, -1):
            a.append(i-j)
            b.append(j)
        for j in range (1, i, +1):
            a.append(j)
            b.append(i-j)
    else: # i 짝수 : 분자 정방향, 분모 역방향
        for j in range (1, i, +1):
            a.append(i-j)
            b.append(j)
        for j in range (1, i, -1):
            a.append(j)
            b.append(i-j)
print(a[x-1],b[x-1],sep=('/'))
'''