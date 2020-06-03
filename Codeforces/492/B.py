n,l = map(int,input().split())
nums = sorted(list(map(int,input().split())))
maxi = 0
for i in range(n - 1):
    maxi = max(maxi, nums[i + 1] - nums[i])
maxi = max(maxi / 2, nums[0], l - nums[n - 1])
print("%.10f" % maxi)