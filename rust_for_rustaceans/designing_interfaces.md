* characteristics

## unsuprising api

follow naming and behavior practices

e.g iter(...) -> fn iter(&self) -> Iter 

if you see struct SomethingError -> impl Error {}

check this blog

=> https://dev.to/cthutu/rust-5-naming-conventions-3cjf


common traits for types

e.g  Implement Debug Trait

e.g #[derive(Debug)]
struct

dont disable send and sync and auto-traits

why
! send
* cant be place in mutex
* can be used transitively


!sync


* cant be shared through arc
* can;t be put in staticvariable



implement clone and default

implement partialEq

why ? not difficult
2) enable users to compare values


consider  implementing partialord and hash


what about Eq and ord?
only if additional semantic requirements really apply


deserialize -> optional


## Flexible Api





your code is a contrat constisitn of

requirements
2) promises -> guarantess


## Obvious





check

https://github.com/obi1kenobi/cargo-semver-checks



see deref borrow cow

https://dev.to/zhanghandong/rust-concept-clarification-deref-vs-asref-vs-borrow-vs-cow-13g6

