# 6085 : [기초-종합] 그림 파일 저장용량 계산하기(py)
w, h, b = map(int,input().split())
print("%0.2f MB"%(round(w*h*b/8/1024/1024, 2))) # 소수점 둘째자리까지 반올림해서 출력