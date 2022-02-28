#!/usr/bin/node
function add (a, b) {
    if (isNaN(a) || isNaN(b)) {
        return (NaN);
      } else {
          console.log(parseInt(a) + parseInt(b));
      }
  }
  
add(process.argv[2], process.argv[3]);
