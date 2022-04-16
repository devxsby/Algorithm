N = int(input()) # 점의 개수
num = []

# 리스트에 좌표 입력
for _ in range(N):
    num.append(list(map(int, input().split())))

# key = lambda를 이용해 정렬할 기준을 x[1] 그리고 x[0]으로 잡음
num.sort(key = lambda x: (x[1], x[0]))

for i in num:
    print(i[0], i[1])
   
   
# 다른 풀이 :(x, y)인 것을 뒤집어 (y, x)한뒤 sort함수로 정렬하고 거꾸로 출력
'''
N = int(input())
num = []

for _ in range(N):
    a, b = map(int, input().split())
    num.append([b, a])
num.sort()

for i in num:
    print(i[1], i[0])


'''