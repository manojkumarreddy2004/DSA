def bs(nums, target, low, high):
    if (low>high):
        return -1
    mid = (low+high)//2
    if (nums[mid]==target):
        return mid
    elif (nums[mid]>target):
        return bs(nums,target, low, mid-1)
    else:
        return bs(nums, target, mid+1, high)


nums = list(map(int, input().split()))
target = int(input())

res = bs(nums, target, 0, len(nums)-1)

print(res)
