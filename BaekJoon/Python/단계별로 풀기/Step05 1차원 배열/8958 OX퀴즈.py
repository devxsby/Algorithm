test = int(input()) 
for _ in range(test):
    answer = list(input())
    score = 0
    cnt = 0
    for i in range (len(answer)):
        if answer[i] == "O":
            cnt += 1
            score = score+ cnt
        elif answer[i] == "X":
            cnt = 0
    print(score)