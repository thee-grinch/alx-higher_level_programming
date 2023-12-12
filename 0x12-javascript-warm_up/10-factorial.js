#!/usr/bin/node

const myNum = Number(process.argv[2]);

function factorial (n) {
  if (!n) {
    return 1;
  }
  if (n === 0) {
    return 1;
  }
  return (n * factorial(n - 1));
}
console.log(factorial(myNum));
