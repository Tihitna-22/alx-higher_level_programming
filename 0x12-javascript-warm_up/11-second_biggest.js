#!/usr/bin/node
let nMax = 0;
let args = process.argv.slice(2);
if (args.length > 1) {
  args.sort();
  Max = args[args.length - 2];
}
console.log(nMax);
