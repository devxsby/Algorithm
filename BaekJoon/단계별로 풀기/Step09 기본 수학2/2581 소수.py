a = int(input())
b = int(input())

prime_number = []

for num in range(a, b+1):
    error = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 num-1까지
            if num % i == 0:
                error += 1
                break  # 2부터 num-1까지 나눈 몫이 0이면 error가 증가하고 for문을 끝냄
        if error == 0:
            prime_number.append(num)  # error가 없으면 소수 리스트에 추가
            
if len(prime_number) > 0 :
    print(sum(prime_number))
    print(min(prime_number))
else:
    print('-1')