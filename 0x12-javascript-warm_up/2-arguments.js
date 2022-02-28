#!/usr/bin/node
let aLen = process.argv.length;
if (aLen === 2) {
  console.log('No argument');
} else if (aLen === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
