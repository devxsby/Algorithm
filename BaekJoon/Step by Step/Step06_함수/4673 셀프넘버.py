# 함수 d(n) : 생성자n을 이용해 d(n)을 만드는 수식
def d (n):
    n = n + sum(map(int,str(n)))
    return n

# 셀프 넘버가 아닌 수들 집합 (생성자 있는 수)
non_selfnum = set()

# non_selfnum 집합에 들어갈 수들 찾아 넣기
for i in range (1, 10001):
    non_selfnum.add(d(i))

# 셀프 넘버 출력
for j in range (1, 10001):
    if j not in non_selfnum:
        print(j)