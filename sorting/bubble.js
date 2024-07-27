function bubbleSort(nums) {
  // code goes here
  for(let i = 0; i < nums.length - 1; i++) {
    for (let j = 0; j < nums.length  - 1 - i; j++) {
      if (nums[j] > nums[j+1]) {
        const temp = nums[j]
        nums[j] = nums[j+1]
        nums[j+1] = temp
      }
    }
  }
  return nums
}

let nums = [9, 10, 1, 2, 4, 5, 3, 6, 7, 8]

console.log(bubbleSort(nums))


function bubbleSort(nums) {
  let swapped 
}
