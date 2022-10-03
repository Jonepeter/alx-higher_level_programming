#!/usr/bin/node
const myArgs = process.argv.slice(2);
const n = Number(myArgs[0]);
let x = '';
if (isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      x += 'X';
    }
    console.log(x);
    x = '';
  }
}
