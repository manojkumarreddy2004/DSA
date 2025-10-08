# Same as rotated_sorted_array but the only change is that the array may contain duplicates
# Output should be true if the target is present in the array else false``
# Example 1 arr=[2, 2, 2, 2, 3, 2,2,2] target=3 output=true

def rotated_sorted_array2(arr, target):
    low, high, res, = 0, len(arr)-1, False 
    
    while (low<=high):
        mid = (low+high)//2
        if (arr[mid]==target):
            res = True
            break
        if (arr[low]==arr[mid]==arr[high]):
            low += 1
            high -=1
        elif (arr[low]<=arr[mid]):
            if (target<=arr[mid] and target>=arr[low]):
                high = mid-1
            else:
                low = mid+1
        elif (arr[mid]<=arr[high]):
            if (target>=arr[mid] and target<=arr[high]):
                low = mid+1
            else:
                high = mid-1
    return res

arr = list(map(int, input().split()))
target = int(input())

res = rotated_sorted_array2(arr, target)

print(f'Position of {target} in {arr} is : {res}')
