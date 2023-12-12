#!/usr/bin/node

let largest = 0;
let second = 0;

for (let i = 0; i < process.argv.length; i++) {
	let myInt = Number(process.argv[i]);
	if (myInt > largest) {
		second = largest;
		largest = myInt;
	}
}
console.log(second);
