#!/usr/bin/node
const myArgs = process.argv.slice(2);
const l = myArgs.length;
let a;
if (l === 0) {
  a = 'No argument';
} else if (l === 1) {
  a = 'Argument found';
} else {
  a = 'Arguments found';
}
console.log(a);
