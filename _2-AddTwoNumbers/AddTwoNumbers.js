/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

//My instinctive method
var twoSum = function(nums, target) {
    let temp =[]
    for (i =0 ; i<nums.length;i++){
for (j=i+1; j<nums.length;j++){
    if(nums[i]+nums[j] === target){
        temp.push(i,j)
    }
}
    }

    return temp
};