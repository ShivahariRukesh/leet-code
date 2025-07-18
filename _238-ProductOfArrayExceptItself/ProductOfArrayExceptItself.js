/**
 * @param {number[]} nums
 * @return {number[]}
 */

// My own hectic solution damnnnnn
var productExceptSelf = function(nums) {
    
    let newArr =[]
    let product=1;
    let flag=0;
    let zero =0
    let doubleZero =0;
    nums.forEach((num)=>{
        
        if(num===0)
        {
            if(doubleZero===1){
                product=0
            }
            product =product*1
            flag=1;
        doubleZero=1
        }else{
    
    product = product * num
    zero =1
        }
    })
    
    if(zero===0){
    
        nums.forEach(num=> newArr.push(0))
    
        return newArr
    }
        for (i =0;i<nums.length;i++){
    
            if(flag===1){
           if(nums[i]===0){
                newArr.push(product)
            }
            else{
    newArr.push(0)
            }
            }
            else
            {
    
            if(nums[i]===0){
                newArr.push(product)
            }
            else{
    newArr.push(product/nums[i])
            }
        }
            }
    
        return newArr
    };