#!/usr/bin/node
function add (x, y) {
  return x + y;
}

const myArgs = process.argv.slice(2);
const n1 = Number(myArgs[0]);
const n2 = Number(myArgs[1]);
console.log(add(n1, n2));
