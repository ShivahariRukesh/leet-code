/**
 * @param {number[]} values
 * @return {number}
 */

// my solution but time exceed err is seen
var maxScoreSightseeingPair = function(values) {
    
    let max= 0;
    let calc;
    for (i=0; i<values.length-1;i++){
        for (j =i+1; j<values.length;j++){

calc = values[i] + values[j] +i-j
if(max<calc){
    max = calc
}
        }
    }
    return max;
};