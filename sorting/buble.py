

def bubbleSort(nums):
    """
    Bubble Sort = pairs of element are compared, and the elements swapped 
    if they are not in order
    O(n^2)
    Space Complexity: n


    First it loop through the array 1 time. 
    Then swap that the highest to the end of array
    then in inner loop it which is does not need to swap last ele that have already swapped
    (len(nums) - 1 - i) 
    Compare pair val then stored in temporary values then swap if the current j val greater than j + 1 swap.
    """
    for i in range(0, len(nums) -1):
      for j in range(0, len(nums) - 1 - i):
        if nums[j] > nums [j+ 1]:
          temp = nums[j]
          nums[j] = nums[j+1]
          nums[j + 1] = temp
    return nums
nums = [10, 5, 3, 8, 2, 6, 4, 7, 9, 1]
print(bubbleSort(nums)) #[1, 2, 3, 4, 5, 6, 7, 8, 9]