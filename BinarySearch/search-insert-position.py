# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# 
# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#
# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4


def search_insert_position(arr, target):
    low, high,res = 0, len(arr)-1, len(arr)

    while (low<=high):
        mid = (low+high)//2
        if (arr[mid]>=target):
            res = mid
            high = mid-1
        else:
            low = mid+1
    return res

arr = list(map(int, input().split()))
target = int(input())

res = search_insert_position(arr, target)

print(f'Insert Position is : {res}')

