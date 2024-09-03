'''
i = int(input())
num = list(map(int, input().split()))
sortnum = sorted(num)
cnt = 0
for k in range(0, i):
    if num != sortnum:
        for j in range(0, i-k-1):
            if num[j] > num[j+1]: num[j], num[j+1], cnt = num[j+1], num[j], cnt + 1
    else:
        break
print(cnt)
'''

def merge(left, right):
    global cnt
    i, j, temp = 0, 0, []
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            temp.append(right[j])
            j += 1
            cnt += len(left) - i
        else:
            temp.append(left[i])
            i += 1
    return temp + left[i:] + right[j:]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


n = int(input())
cnt = 0
arr = list(map(int, input().split()))
merge_sort(arr)
print(cnt)