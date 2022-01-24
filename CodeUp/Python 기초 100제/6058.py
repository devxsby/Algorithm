# 6058 : [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기(py)
a, b = map(int,input().split())
print(bool((not a and not b))) 
# print(bool(not(a or b)))

# a b    ?
# 0 0    1
# 0 1    0
# 1 0    0
# 1 1    0