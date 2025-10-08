def min_in_rotated_sorted_array(arr):

    low, high, res = 0, len(arr)-1, arr[0]

    while (low<=high):
        mid = (low+high)//2

        if (arr[low]<=arr[mid]):
            if (arr[low]<res):
                res = arr[low]
            low = mid+1
        elif (arr[mid]<=arr[high]):
            if (arr[mid]<res):
                res = arr[mid]
            high = mid-1
    return res


arr = list(map(int, input().split()))

res = min_in_rotated_sorted_array(arr)

print(f'Minimun in the {arr} is : {res}')
