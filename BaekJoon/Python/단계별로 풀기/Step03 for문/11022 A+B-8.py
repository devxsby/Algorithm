case = int(input())

for i in range(1,case+1):
    a,b = map(int,input().split())
    print("Case #"+str(i)+':',a,'+',b,'=',a+b)
    
# "Case #x: A + B = C"