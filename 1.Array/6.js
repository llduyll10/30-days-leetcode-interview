/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k){
    k = k % nums.length
    let result = []

    for(let i=0; i< nums.length; i++){
        let newIdx = (i+k) % nums.length
        console.log('i',i)
        console.log('newIdx',newIdx)
        result[newIdx] = nums[i]
    }

    for(let i=0; i< nums.length; i++){
        nums[i] = result[i]
    }
}

// Driven code
// Input: nums = [1,2,3,4,5,6,7], k = 3
// Output: [5,6,7,1,2,3,4]
// Explanation:
// rotate 1 steps to the right: [7,1,2,3,4,5,6]


let nums = [1,2,3,4,5,6,7], k = 3
rotate(nums,k)
console.log(nums)