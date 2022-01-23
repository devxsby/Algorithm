# 6054 : [기초-논리연산] 둘 다 참일 경우만 참 출력하기(설명)(py)
a, b = input().split()
print(bool(int(a)) and bool(int(b)))

# a b   a&&b
# 0 0    0
# 0 1    0
# 1 0    0
# 1 1    1