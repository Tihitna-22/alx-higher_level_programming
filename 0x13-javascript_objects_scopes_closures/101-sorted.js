#!/usr/bin/node

const oldDict = require('./101-data.js').dict;
const newDict = {};
Object.keys(oldDict).forEach(function (key) {
  if (newDict[oldDict[key]] === undefined) {
    newDict[oldDict[key]] = [];
  }
  newDict[oldDict[key]].push(key);
});
console.log(newDict);
