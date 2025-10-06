#lower bound - smallest index i such that arr[i]>=target
#example input 1 arr = [1,2,3,4,5,6,10] target = 6 output=5
#example input 2 arr=[1,2,3,4,5, 10] target = 6 output=5

#Note: If all the elements in the arr are smaller than target then lower bound considered to be n=length of the arr

#expected tc - O(log n)

def lower_bound(arr, target, low, high, res):
    if (low>high):
        return
    mid = (low+high)//2
    if (arr[mid]>=target):
        res[0] = mid
        lower_bound(arr, target, low, mid-1, res)
    elif (arr[mid]<target):
        lower_bound(arr, target, mid+1, high, res)

nums = list(map(int, input().split()))
target = int(input())
res = [len(nums)]

lower_bound(nums, target, 0, len(nums)-1, res)

print(res[0])


