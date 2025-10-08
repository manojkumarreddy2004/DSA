#Print the No of Occurances of a NUmber in the given array 

#Example 1 Input = [1, 2, 3 , 3, 4] target=3 output = 2
#Example 2 input = [1, 2, 3, 4] target = 5 output=0


import bisect

def no_of_occurances(arr, target):
    #INbuilt Function to calculate lower bound of an element in an array
    lbi = bisect.bisect_left(arr, target)
    #inbuilt function to calculate the upper bound of an element in an array
    ubi = bisect.bisect_right(arr,target)

    return ubi-lbi

arr = list(map(int, input().split()))
target = int(input())

res = no_of_occurances(arr, target)

print(f'No of Occurances of {target}: {res}')
