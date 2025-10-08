#Find the first and last occurance of a number in a given list 

#Example 1 Input = [1, 2, 2, 3, 4] target = 2 output = [1,2]

#Example 2 Input = [1, 2, 3, 4] target = 2 output = [1,1]

#Example 3 Input = [1, 3, 4] target = 2 output = [-1,-1]


def first_occur(arr, target):
    low, high, res = 0, len(arr)-1, -1
    while (low<=high):
        mid = (low+high)//2
        if (arr[mid]==target):
            res = mid
            high = mid-1
        elif (arr[mid]>target):
            high = mid-1
        else:
            low = mid+1
    return res


def last_occur(arr,target):
    low, high, res = 0, len(arr)-1, -1
    
    while (low<=high):
        mid = (low+high)//2
        if (arr[mid]==target):
            res = mid
            low = mid+1
        elif (arr[mid]>target):
            high = mid-1
        else:
            low = mid+1
    return res
arr = list(map(int, input().split()))
target = int(input())
res = [first_occur(arr, target), last_occur(arr, target)]
print(f'First and Last Occurance of {target} : {res}')
