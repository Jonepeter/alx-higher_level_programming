#!/usr/bin/node
function factorial (x) {
  if (x === 1 || isNaN(x)) {
    return (1);
  }
  return (factorial(x - 1) * x);
}

const myArgs = process.argv.slice(2);
const n1 = Number(myArgs[0]);
console.log(factorial(n1));
