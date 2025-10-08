
# Searching for an element in Rotated Sorted Array

# Example 1 Input arr = [4, 3, 1, 2] target = 3  Output = 1

# Example 2 Input arr = [5, 4, 1, 2, 3] target = 6  Output = -1

#It is guaranteed that array contains only unique elements

def rotated_sorted_array(arr, target):
    low, high, res = 0, len(arr)-1, -1

    while (low<=high):
        mid = (low+high)//2
        if (arr[mid]==target):
            res = mid
            break
        # checking if Left Part is Sorted
        elif (arr[mid]>arr[low]):
            # Checking if target present in left Part and if yes move to left search space
            if (target>=arr[low] and target<=arr[mid]):
                high = mid-1
            #Move to right search space 
            else:
                low = mid+1
        # Checking if right search space is sorted 
        elif (arr[mid]<arr[high]):
            #Checking if target is present in the right search space and if yes move to right search space by updating low to mid+1
            if (target>=arr[mid] and target<=arr[high]):
                low = mid+1
            # Else Move to left search space 
            else:
                high = mid-1

        #returning the result
    return res



arr = list(map(int,input().split()))

target = int(input())

res = rotated_sorted_array(arr, target)

print(f'Index of {target} in {arr} is : {res}')


