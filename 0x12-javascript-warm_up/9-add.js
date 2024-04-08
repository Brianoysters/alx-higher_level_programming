#!/usr/bin/node
/*prints summation of two int*/
function add (m, n) {
  const letter = m + n;
  console.log(letter);
}

add(Number(process.argv[2]), Number(process.argv[3]));
