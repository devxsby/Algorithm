# 6040 : [기초-산술연산] 정수 2개 입력받아 나눈 몫 계산하기(설명)(py)
a, b = input().split()
c = int(a)//int(b)
print(c)

"""
    실험
    case1) 16 sec
    a, b = input().split()
    c = int(a)//int(b)
    print(c)
    
    case2) 17sec
    a,b = map(int,input().split())
    print(a//b)
    
    case3) 21sec
    a,b = input().split()
    print(int(a)//int(b))
"""