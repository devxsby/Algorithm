# 6055 : [기초-논리연산] 하나라도 참이면 참 출력하기(설명)(py)
a, b = map(int,input().split())
print(bool(int(a) or int(b)))

# a b  a&&b
# 0 0    0
# 0 1    1
# 1 0    1
# 1 1    1