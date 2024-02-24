#!/usr/bin/node
exports.converter = function (base) {
  function getNumber (number) {
    return number.toString(base);
  }
  return getNumber;
};
