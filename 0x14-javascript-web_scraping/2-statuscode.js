#!/usr/bin/node
const request = require('request');
const response = request(process.argv[2]);
console.log(response.statusCode);
