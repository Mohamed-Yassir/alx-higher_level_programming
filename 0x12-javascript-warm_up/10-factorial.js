#!/usr/bin/node
// computes and prints a factorial
let argss = parseInt(process.argv[2]);
if (isNaN(argss)) {
  argss = 1;
}
function recursiveFactorial (n) {
  if (n === 1) {
    return 1;
  }
  return (n * recursiveFactorial(n - 1));
}
console.log(recursiveFactorial(argss));
