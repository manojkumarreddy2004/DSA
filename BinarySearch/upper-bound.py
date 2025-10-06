#upper bound - index of initial value that surpasses the target or simply index os arr[i]>target

def upper_bound(arr, target):
    low, high, res = 0, len(arr)-1, len(arr)

    while (low<=high):
        mid = (low+high)//2
        if (arr[mid]<=target):
            low = mid+1
        else:
            res = mid
            high = mid-1
    return res
    
    

arr = list(map(int, input().split()))
target = int(input())

res = upper_bound(arr, target)

print(res)
