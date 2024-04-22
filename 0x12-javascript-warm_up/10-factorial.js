#!/usr/bin/node
// computes and prints a factorial

const factorial = n => isNaN(n) ? 1 : (n <= 1 ? 1 : n * factorial(n - 1));

console.log(factorial(parseInt(process.argv[2])));
