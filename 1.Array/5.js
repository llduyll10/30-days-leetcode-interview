/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums){
    let count = 0
    let candidate = null

    for(let num of nums){
        if(count === 0){
            candidate = num
        }

        if(num === candidate){
            count++
        }else{
            count--
        }
    }

    return candidate
}

// Driven code
// Input: nums = [2,2,1,1,1,2,2]
// Output: 2

let nums = [2,2,1,1,1,2,2]

console.log(majorityElement(nums))