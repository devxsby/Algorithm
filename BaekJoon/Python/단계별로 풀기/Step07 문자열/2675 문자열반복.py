t = int(input()) # 테스트 케이스 개수

for _ in range(t):
    n, s = input().split() # n: 반복횟수, s:입력 문자열
    for i in s:
        print(int(n)*i, end = '') # end를 넣어서 자동줄바꿈 방지
    print()