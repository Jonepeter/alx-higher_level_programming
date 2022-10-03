#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs.length <= 1) {
  console.log(0);
} else {
  for (let i = 0; i < myArgs.length; i++) {
    if (Number(myArgs[i]) === Math.max(...myArgs)) {
      myArgs.splice(i, 1);
      break;
    }
  }
  console.log(Math.max(...myArgs));
}
