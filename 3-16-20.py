"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

"""
Brute Force Solution:
    Loop through the array and add each number until I get my desired K value. Not very efficient.

Good Solution:
    Hash Table

Edge Cases to think about:
    - K appears twice
    - List is empty
    - K doesn't appear
"""

def getnums(nums, k):
    # Create an empty hash set
    s = set()
    # loop through the nums array
    for i in range(0,len(nums)):
        # make temporary varaible by subtracting temp to number in array
        temp = k-nums[i]
        # check if temp is in hash set
        if (temp in s):
            return (nums[i], temp)
        # If it is not then add it to hashset 
        s.add(nums[i])

print("Hello World From Solution")
nums = [10, 15, 3, 7]
k = 17
print("Pair with sum which adds to " +str(k)+" is:")
adders = getnums(nums, k)
print(adders)
