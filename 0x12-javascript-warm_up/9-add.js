#!/usr/bin/node


function add(a, b) {
 if (isNaN(a) || isNaN(b)) {
    return (NaN);
  } else {
    return (parseInt(a) + parseInt(b));
  }
}

console.log (add (process.argv[2], process.argv[3]))
