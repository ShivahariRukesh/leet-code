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


//This is the optimal solution where just only a little hint was enough


var maxScoreSightseeingPair = function(values) {
    
    let max1= -Infinity;


  let calc1;
  let calc2;

  let i=1

  let currentIValue = values[0]
  while(i <values.length){

      
calc2 = values[i] - i;
if(calc2+currentIValue > max1){
  max1 = calc2+currentIValue
}

calc1 = values[i] + i;
if(currentIValue<calc1){
currentIValue = calc1
}




 i++;     
  }
  
  return max1;
};