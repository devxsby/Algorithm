numbers  = []

for _ in range(9):
    num = int(input())
    numbers.append(num)

print(max(numbers))  # max 메소드 이용
print(numbers.index(max(numbers))+1)