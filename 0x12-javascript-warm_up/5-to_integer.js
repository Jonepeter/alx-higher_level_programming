#!/usr/bin/node
const myArgs = process.argv.slice(2);
const n = Number(myArgs[0]);
if (isNaN(n)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + n);
}
