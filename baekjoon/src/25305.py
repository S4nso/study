n, k = map(int, input().split())
rank = sorted(list(map(int, input().split())), reverse=True)
print(rank[k-1])