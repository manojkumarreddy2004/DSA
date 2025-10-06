#Ceil is the number in the array which is the first number  greater than or equal to target 
#If array does not contain any element which is >=target then ceil would be -1 

#Example 1 Input: [1, 2, 3, 4, 7] target=6 output=7
#Example 2 Input: [1, 2, 3, 4, 7] target = 7 output = 7
#Example 3 Input: [1, 2, 3, 4] target = 7 output = -1

def findceil(arr, target):
    low, high, res = 0, len(arr)-1, -1
    while (low<=high):
        mid = (low+high)//2
        if (arr[mid]>=target):
            res = arr[mid]
            high = mid-1
        else:
            low = mid+1
    return res
arr = list(map(int,input().split())))
target = int(input())

res = findceil(arr, target)

print(f'Ceil of {target} : {res}')
