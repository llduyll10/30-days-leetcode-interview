/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */

function mergeSort(arr){
    if(arr.length <=1){
        return arr
    }
    let middle = Math.floor(arr.length / 2)
    let left = arr.slice(0,middle)
    let right = arr.slice(middle)
    return mergeSortArray(mergeSort(left), mergeSort(right))
}

function mergeSortArray(left, right){
    let result = []
    let leftIdx = 0
    let rightIdx = 0

    while(leftIdx < left.length && rightIdx < right.length){
        if(left[leftIdx] < right[rightIdx]){
            result.push(left[leftIdx])
            leftIdx++
        }
        else{
            result.push(right[rightIdx])
            rightIdx++
        }
    }

    while(leftIdx<left.length){
        result.push(left[leftIdx])
        leftIdx++
    }

    while(rightIdx<right.length){
        result.push(right[rightIdx])
        rightIdx++
    }
    return result
}

var merge = function (nums1, m, nums2, n){
    let nums1Part = nums1.slice(0,m)
    let nums2Part = nums2.slice(0,n)

    let sortedArr = mergeSort(nums1Part.concat(nums2Part))

    for(let i=0; i<sortedArr.length; i++){
        nums1[i] = sortedArr[i]
    }
}

// Driven Code
// Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
// Output: [1,2,2,3,5,6]
// Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
// The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

let nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

merge(nums1, m, nums2, n)
console.log(nums1)