const num= 1679583;
const lim = 9;

const sumDigit = (num, sum = 0) => {
   if(num){
      return sumDigit(Math.floor(num / 10), sum + num % 10);
   };
   return sum;
};
const persistence = num => {
   num = Math.abs(num);
   let res = 0;
   while(num > lim){
      num = sumDigit(num);
      res++;
   };
   return res;
};
console.log(persistence(num));