#!/usr/bin/node
// SCRIPT that prints a sequare
const sQx = 'X';
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(sQx.repeat(parseInt(process.argv[2])));
  }
}
