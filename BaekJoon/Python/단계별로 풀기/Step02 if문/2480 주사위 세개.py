a, b, c = map(int, input().split())
max_num = (max(a, b, c))
if a == b and b== c:
    print(10000 + a*1000)
elif a == b or b == c or a == c:
    if a == b:
        print(1000+ a*100)
    elif b == c:
        print(1000+ b*100)
    else:
        print(1000+ c*100)
else:
    print(max_num*100)