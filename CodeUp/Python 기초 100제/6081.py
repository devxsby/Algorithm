# 6081 : [기초-종합] 16진수 구구단 출력하기(py)
n = int(input(),16)
for i in range (1,16):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')