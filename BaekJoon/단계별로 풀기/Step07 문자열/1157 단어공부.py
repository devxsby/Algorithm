word = input().upper() # 입력받은 문자열 대문자로 변환
set_words = list(set(word)) # 중복값 제거한 문자열

cnt_list = []
for i in set_words :
    cnt = word.count
    cnt_list.append(cnt(i)) # count 숫자를 리스트에 append
    
if cnt_list.count(max(cnt_list)) > 1 : # count 숫자 최대값이 중복됐을 때
    print('?')
else : 
    max_index = cnt_list.index(max(cnt_list)) # count 숫자 최대값 위치 
    print(set_words[max_index]) 