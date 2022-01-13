a, b = input().split() # input()은 입력받는 모든것을 문자열로 취급함

a = int(a[::-1]) # 리스트 슬라이싱해서 내용 뒤집기
b = int(b[::-1])

if a > b:
    print(a)
else:
    print(b)