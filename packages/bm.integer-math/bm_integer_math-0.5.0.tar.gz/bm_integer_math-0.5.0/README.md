# Daddy's boring math library - integer math package

Package of Python integer math libraries.

Part of the "Boring Math" PyPI **bm** namespace for mathematical hobby
projects.

* [Number Theory Module](#number-theory)
* [Combinatorics module](#combinatorics)

* **Repositories**
  * [bm.integer-math][1] project on *PyPI*
  * [Source code][2] on *GitHub*
* **Detailed documentation**
  * [Detailed API documentation][3] on *GH-Pages*

## Library Modules

### Number Theory Module: 

* Number Theory
  * Function **gcd**(int, int) -> int
    * greatest common divisor of two integers
    * always returns a non-negative number greater than 0
  * Function **lcm**(int, int) -> int
    * least common multiple of two integers
    * always returns a non-negative number greater than 0
  * Function **coprime**(int, int) -> tuple(int, int)
    * make 2 integers coprime by dividing out gcd
    * preserves signs of original numbers
  * Function **iSqrt**(int) -> int
    * integer square root
    * same as math.isqrt
  * Function **isSqr**(int) -> bool
    * returns true if integer argument is a perfect square
  * Function **primes**(start: int, end: int) -> Iterator[int]
    * now using *Wilson's Theorem*
  * Function **legendre_symbol**(a: int, p: int) ->datastructures int
    * where `p > 2` is a prime number
  * Function **jacobi_symbol**(a: int, n: int) -> int
    * where `n > 0`

---

### Combinatorics Module: **bm.integer_math.combinatorics**

* Combinatorics 
  * Function **comb**(n: int, m: int) -> int
    * returns number of combinations of n items taken m at a time
    * pure integer implementation of math.comb

---

[1]: https://pypi.org/project/bm.integer-math/
[2]: https://github.com/grscheller/bm-integer-math/
[3]: https://grscheller.github.io/boring-math-docs/integer-math/

