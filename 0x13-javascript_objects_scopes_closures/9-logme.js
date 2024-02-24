#!/usr/bin/node
exports.logMe = function (item) {
  console.log(`${item}: ${exports.logMe.count}`);
  exports.logMe.count++;
};
