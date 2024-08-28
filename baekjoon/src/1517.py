i = int(input())
num = list(map(int, input().split()))
#sortnum = sorted(num)
cnt = 0
for k in range(0, i):
    #if num != sortnum:
        for j in range(0, i-k-1):
            if num[j] > num[j+1]: num[j], num[j+1], cnt = num[j+1], num[j], cnt + 1
    #else:
    #    break
print(cnt)