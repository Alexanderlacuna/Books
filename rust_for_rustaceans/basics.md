


# rust basics


Ahead of time compilation

look at package definition via YAML VS TOML vs JSON


target/debug/main 
target/release/main


* looking at random number generatorsx

notes on random number generator


https://www.redhat.com/en/blog/understanding-random-number-generators-and-their-limitations-linux

entrophy



* variables


declaring variables use keyword let 
let is by default immutable
that means on binding a value to a variable 
let say let x = 4;
the value of x will always be 4 unless we drop x
to make val of x mutable we use mut 
let mut x = 4;
x = x+1

constants defined const keyword live as long as the scope  of their declaration
are not default as immutable but are always immutable
you must annotate the type
const expression evaluated at compile time not evaluated at run time
const TOTAL_SECONDS:usize = 60*60
syntax: uppercase+snake_case
TOTAL_TIME