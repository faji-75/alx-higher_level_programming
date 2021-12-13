#!/usr/bin/node

const args = Math.floor(Number(process.argv[2]));
if (isNaN(args)) {
  console.log('Missing number of occurrences');
} else {
  for (let arg = 0; arg < args; arg++) {
    console.log('C is fun');
  }
}
