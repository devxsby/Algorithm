n = int(input()) # 68
num = n
cnt = 0          # 사이클 수

while True:
    a = num//10  # 십의 자리 6
    b = num%10   # 일의 자리 8
    c = (a+b)%10 # 6 + 8 = 1"4"
    num=(b*10)+c # 80 + 4 = 84
    
    cnt = cnt+1  
    if (num==n):
        break
print(cnt)