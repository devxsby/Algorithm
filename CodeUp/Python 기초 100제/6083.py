# 6083 : [기초-종합] 빛 섞어 색 만들기(설명)(py)
r, g, b = map(int,input().split())
for x in range (0,r):
    for y in range (0,g):
        for z in range (0,b):
            print(x,y,z)
print(r*g*b)