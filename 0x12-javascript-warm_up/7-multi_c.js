#!/usr/bin/node
const myArgs = process.argv.slice(2);
const n = Number(myArgs[0]);
if (isNaN(n)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
}
