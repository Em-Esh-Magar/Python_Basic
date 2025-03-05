n = int(input())
arr = list(map(int, input().split()))

num = list(set(arr))

num.sort(reverse=True)

print(num[1])
