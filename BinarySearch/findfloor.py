def findfloor( arr, target):
    low, high, res = 0, len(arr)-1, -1

    while (low<=high):
        mid = (low+high)//2

        if (arr[mid]<=target):
            res = arr[mid]
            low = mid+1
        else:
            high = mid-1
    return res



arr = list(map(int,input().split()))
target = int(input())

res = findfloor(arr, target)

print(f'Floor of {target} : {res}')
