# 6083 : [기초-종합] 빛 섞어 색 만들기(설명)(py)
a, b, c = map(int,input().split())
for x in range (0,a):
    for y in range (0,b):
        for z in range (0,c):
            print(x,y,z)
print(a*b*c)