/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums){
    if(nums.length === 0) return 0

    let k = 1
    let count = 1

    for(let i=1; i<nums.length; i++){
        if(nums[i] !== nums[i-1]){
            nums[k] = nums[i]
            k++
            count = 1
        }
        else{
            if(count < 2){
                nums[k] = nums[i]
                k++
                count++
            }
        }
    }
    return k
}

// Driven Code
// Input: nums = [1,1,1,2,2,3]
// Output: 5, nums = [1,1,2,2,3,_]

// Input: nums = [0,0,1,1,1,1,2,3,3]
// Output: 7, nums = [0,0,1,1,2,3,3,_,_]

let nums = [1,1,1,2,2,3]
console.log(removeDuplicates(nums))
console.log(nums)
