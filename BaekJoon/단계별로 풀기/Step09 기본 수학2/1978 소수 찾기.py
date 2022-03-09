# 에라토스테네스의 체 알고리즘 2
def isPrime(n):
	if n <= 1:
		return False
	i = 2
	while i*i <= n:
		if n%i == 0:
			return False
		i += 1
	return True
input()
ans = 0
for n in map(int, input().split()):
	if isPrime(n):
		ans += 1
print(ans)