# 6030 : [기초-값변환] 영문자 1개 입력받아 10진수로 변환하기(설명)(py)
n = ord(input()) #입력받은 문자를 10진수 유니코드 값으로 변환한 후, n에 저장한다.
print(n)

# ord( ) 는 어떤 문자의 순서 위치(ordinal position) 값을 의미한다.  
# 실제로 각각의 문자들에는 연속된 정수 값이 순서에 따라 부여 되어 있다. A:65, B:66, C:67 .... 
# ord(c) : 문자 c 를 10진수로 변환한 값 