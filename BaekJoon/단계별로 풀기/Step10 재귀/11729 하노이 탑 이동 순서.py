def hanoiTower(n, a, b, c):
    if n == 1 :
        print(a, c)
        return
       
    hanoiTower(n - 1, a, c, b) # 1단계
    print(a, c)                 # 2단계
    hanoiTower(n - 1, b, a, c) # 3단계
    
n = int(input())
print(2**n - 1)
hanoiTower(n, 1, 2, 3)