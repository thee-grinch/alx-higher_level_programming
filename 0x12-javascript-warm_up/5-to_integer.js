#!/usr/bin/node

myNum = Number(process.argv[2]);

if (myNum) {
  console.log('My number: ' + myNum);
} else {
	console.log('Not a number');
}
