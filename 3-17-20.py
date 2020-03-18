"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element
at index i of the new array is the product of all the numbers in the
original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
be [2, 3, 6].


arr = [3, 2, 1]
length = 3
temp = arr[0]
for(int i = 1; i < length; i ++){
    temp = temp * arr[i]
}
dummy = []
for (int i = 0; i < length; i++){
    dummy[i] = temp / arr[i]
}



Follow-up: what if you can't use division?
"""
"""
Brute Force Solution:
    Loop through the entire array O(n^2)
"""

def DaMagic(arr, n):
    # In this function the majic happens. Recursive magic
    temp = arr[0] # This gets first val of array
    for i in range(1, len(arr)):
        temp *= arr[i]
    print(temp)
    newArray = []
    for j in range(0, len(arr)):
        dummy = temp / arr[j]
        print("dummy is ", dummy)
        newArray.append(dummy)
    return(newArray)


# Example array
array = [1, 2, 3, 4, 5]
print("Array is: ")
print(array)

# Length of array
lenny = len(array)
newArray = DaMagic(array, lenny)
print("New Array is:")
print(newArray)
