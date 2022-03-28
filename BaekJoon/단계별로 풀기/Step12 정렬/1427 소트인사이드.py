n = int(input())
num_list = list(map(int,str(n)))

num_list.sort(reverse=True) # 내림차순 정렬
 
for i in num_list:
    print(i,end='')