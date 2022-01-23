# 6057 : [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기(설명)(py)
a, b = map(int,input().split())
print(bool((not a and not b) or (a and b)))

# a b    ?
# 0 0    1
# 0 1    0
# 1 0    0
# 1 1    1