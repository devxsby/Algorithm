N = int(input())
member_list = []

for _ in range(N):
    age, name = map(str, input().split())
    age = int(age)
    member_list.append((age, name))

member_list.sort(key = lambda x : x[0])	# (age, name)에서 age만 비교

for i in member_list:
    print(i[0], i[1])