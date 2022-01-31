# 6084 : [기초-종합] 소리 파일 저장용량 계산하기(py)
h, b, c, s = map(int,input().split())
print(round(h*b*c*s/8/1024/1024, 1),"MB")