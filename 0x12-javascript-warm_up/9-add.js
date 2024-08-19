#!/usr/bin/node
// print addition of 2 numbers
const first = process.argv[2];
const sec = process.argv[3];
function add (a, b) {
  return a + b;
}
const a = parseInt(first);
const b = parseInt(sec);
console.log(add(a, b));
