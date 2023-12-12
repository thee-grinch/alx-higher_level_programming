#!/usr/bin/node

const size = Number(process.argv[2]);
let row = '';

if (size) {
  for (let i = 0; i < size; i++) {
    row += 'X';
  }
  for (let j = 0; j < size; j++) {
    console.log(row);
  }
} else {
  console.log('Missing size');
}
