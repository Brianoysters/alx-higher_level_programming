#!/usr/bin/node
/* prints a square*/
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const m = Number(process.argv[2]);
  let index = 0;
  while (index < m) {
    console.log('X'.repeat(m));
    index++;
  }
}
