/**
 * @param {number[]} prices
 * @return {number}
 */

//My instinctive solution but time limit exceeded
var maxProfit = function(prices) {
    let maxProfit=0;
 
   for (i =0 ; i<prices.length-1; i++){
 
     for (j =i; j<prices.length;j++){
     
     if(prices[j]- prices[i]> maxProfit)
 maxProfit = prices[j] - prices[i]
 
     }
   }
   return maxProfit
 };



 //Optimized solution
var maxProfit = function(prices) {
    let maxProfit=0;
     let minValue = undefined
   for (i =0 ; i<prices.length; i++){
     if (minValue ===undefined || prices[i]< minValue){
         minValue = prices[i]
     }
     if(maxProfit < prices[i]-minValue){
         maxProfit = prices[i]-minValue
     }
   }
   return maxProfit;
 };