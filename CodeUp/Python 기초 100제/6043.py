# 6043 : [기초-산술연산] 실수 2개 입력받아 나눈 결과 계산하기(py)
f1, f2 = input().split()
n = float(f1)/float(f2)
print(format(n,".3f"))  # 소숫점 셋째자리까지 반올림해서 보여줌