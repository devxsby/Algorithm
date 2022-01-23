# 6056 : [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기(설명)(py)
a, b = map(int,input().split())
bool_a = bool(int(a))
bool_b = bool(int(b))
print((bool_a and(not bool_b)) or ((not bool_a) and bool_b))

# a b  (a&&!b)|(!a&&b)
# 0 0         0
# 0 1         1
# 1 0         1
# 1 1         0