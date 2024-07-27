# Problem 2239: Find the closest Number to zero

def closest_to_zero(numbers):
    closest = numbers[0]
    for number in numbers:
        if abs(number) < abs(closest):
            closest = number
        elif abs(number) == abs(closest) and number > closest: 
            # when two close number in the array, return the largeset by
            # take number > closest
            closest = number 
    return closest

# My solution 
def closest_to_zero(nums):
    closest = nums[0]
    for i in nums:
        if abs(i) < abs(closest):
            closest = i
    if closest < 0 and abs(closest) in nums:
        return abs(closest)
    else:
        return closest


# Test Cases
print(closest_to_zero([8, 5, 10])) # 5
print(closest_to_zero([5, 4, -9, 6, -10, -1, 8])) # -1
print(closest_to_zero([8, 2, 3, -2])) # 2
print(closest_to_zero([2, 0])) # 0
print(closest_to_zero([0, 0])) # 0

# Time Complexity: O(n)
# Space Complexity: O(1)



# First step is to iteate throught the array and find the closest number to zero
# Second step: stores the closest number to zero in a variable called closest



