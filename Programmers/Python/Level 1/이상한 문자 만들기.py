# 이상한 문자 만들기
def solution(s):
    answer = []
    s = s.split(' ')

    for i in range(len(s)):
        result = ''
        for j in range(len(s[i])):
            if j % 2 == 0:
                result += s[i][j].upper()
            else:
                result += s[i][j].lower()

        answer.append(result)

    return ' '.join(answer)