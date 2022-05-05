N = int(input())
word_list= []

for i in range(N):
    word_list.append(input())
set_list = set(word_list)	# set으로 변환해서 중복값을 제거
word_list = list(set_list)	# 다시 word_list로 변환
word_list.sort()
word_list.sort(key = len)

for i in word_list:
    print(i)