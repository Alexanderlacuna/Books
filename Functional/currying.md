# Currying
In mathematics and computer science,currying is the techniquer of translating a functional that takes
multiple arguments into sequences of families of functions, each taking a single argument

```math
fx: (X*Y) -> Z   takes two arguments one from X and one from Y,and produces objects in Z

```
the curried form of this functionsl treats the first argument as a parameter so as to create a famuly 
of functions

```math
fx:Y-> Z 

```

this family is arranged so that for  each object x In X,there is exact one function fx



In this example,curry itself becomes a function,that that takes f as an argument and return a function that map each x to Fx.The proper notatin for expressing this  verbose
The function f belongs to the set of functions (X x Y)


function name = (a) => (b) => a + b
Meanqhile Fx belongs to the set of functions Y->Z

Thus,something that map x to Fx will be of the type

X=> [Y=> Z]

With this notation,curry is a functional that takes object from the first set and return ovjects in the second set

curry: [(X *Y)-> Z]-> (X-> [Y->Z])
```math

Given a function

    f : ( X × Y ) → Z f \colon (X \times Y) \to Z ,

currying constructs a new function

    g : X → ( Y → Z ) {\displaystyle g\colon X\to (Y\to Z)}.

That is, g g takes an argument of type X X and returns a function of type Y → Z {\displaystyle Y\to Z}. It is defined by

    g ( x ) ( y ) = f ( x , y ) {\displaystyle g(x)(y)=f(x,y)}

for x x of type X X and y y of type Y Y. We then also write

    curry ( f ) = g . {\displaystyle {\text{curry}}(f)=g.}



```



In Lambda calculus.Functions can only take one paramater:


\x->x+1

\x =>\y->x+y


```
\x \y -> x+y
```



```
add:: Int-> Int-> Int

add x y = x+y

The type signature is right-assocaitve

```

All Type of signatures have implied parenthesesis that
are right-associatve


```
add:::Int => (Int->Int)
add x y = x+y
```


```
add3: int -> (int->(int -> int))

add3 x y z = x+y+z

```