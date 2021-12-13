#!/usr/bin/node

const args = Math.floor(Number(process.argv[2]));
if (isNaN(args)) {
  console.log('Missing size');
} else {
  for (let arg = 0; arg < args; arg++) {
    console.log('X'.repeat(args));
  }
}
