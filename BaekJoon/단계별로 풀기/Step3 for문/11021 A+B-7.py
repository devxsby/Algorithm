case = int(input())
for i in range (1,case+1):
    a, b = map(int,input().split())
    print("Case #"+str(i)+':',a+b)
    
# 띄어쓰기 주의 !

#another solution
"""
cases = int(input())
for i in range(cases):
    a,b = map(int, input().split())
    ans = a + b
    print("Case #%s: %s"%(i+1, ans ))
"""