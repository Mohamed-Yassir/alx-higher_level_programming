#!/usr/bin/node
// Prints -my number: <first argument converted in integer>
// if the first argument can be converted to an integer
if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + (process.argv[2]));
}
