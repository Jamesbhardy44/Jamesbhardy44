var num = 271;
const isDisarium = num => {
   const result = String(num)
   .split("")
   .reduce((acc, val, ind) => {
      acc += Math.pow(+val, ind+1);
      return acc;
   }, 0);
   return result === num;
};
console.log(isDisarium(num));
console.log(isDisarium(23));
console.log(isDisarium(5665));
