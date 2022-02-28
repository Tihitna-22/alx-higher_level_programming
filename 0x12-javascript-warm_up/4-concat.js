#!/usr/bin/node
let aLen = process.argv.length;
let arg = process.argv[2];
let arg2 = process.argv[3];
if (arg === undefined) {
  console.log('undefined is undefined');
} else if (aLen === 3 ){
  console.log(arg + ' is undefined');
}else {
  console.log(arg + ' is ' + arg2);
}
