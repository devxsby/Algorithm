n = int(input())

for _ in range (n):
    nums = list(map(int,input().split()))
    avg = sum(nums[1:])/nums[0] # nums[0]: 학생수, nums[1:] 점수로 평균구함
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1 # 평균 넘는 학생 수 카운트
    rate = cnt/nums[0]*100
    print('%.3f' %rate + '%')