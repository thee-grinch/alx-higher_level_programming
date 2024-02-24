#!/usr/bin/node
const myList = require('./100-data').list;
console.log(myList);
const myMap = myList.map((x, index) => x * index);
console.log(myMap);
