#!/usr/bin/node
// Prints 'x' times "C is fun"
const isFun = 'C is fun';
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(isFun);
  }
}
