# 딕셔너리 추가 공부할 것 !! 
import sys
input = sys.stdin.readline

n = int(input())
dic = {}

nums = list(map(int, input().split()))
sNums = sorted(set(nums))

for i in range(len(sNums)):
    dic[sNums[i]] = i

for j in nums:
    print(dic[j], end=' ')