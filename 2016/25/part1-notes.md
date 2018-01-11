# Part 1: Notes

This can be brute forced, I imagine. My VM was buggy, in terms of providing
reasonable evidence for a repeating sequence such that I ended up going the
analytical route instead.

The program does the following:
* 0-2: initialisation of fixed constants 170 & 15
* 3-7: add 170 * 15 == 2550 to register 'a'
* 8-9: initialise the calculation [register 'a' is our accumulator]
* 10-19: a <- a / 2, integer division; register 'c' holds the remainder
         (sort of)
* 20-26: figure out, from 'c', whether the division had a remainder,
         leaving 1 or 0 in register 'b'
* 27: write out 1 or 0
* 28: if register 'a' isn't 0 yet, then don't re-initialize, just do another
      divide-by-two cycle
* 29: algorithm needs to loop, so fetch the initial value (a + 2550) from
      register 'd', where it's been stashed

So, to generate a sequence of 0, 1, 0, 1, 0, ... we need a number that is
initially even. The result of the division should be odd, then even again,
then odd, and so forth.

The number must also be the next highest number to have this property and
be greater than 2550.

Initially, I thought about:
* some algebraic expression that might satisfy this
* running a set of candidates through that displayed this property

But a / 2 is a shift right by one bit, and the even / odd is a read on the
bit that was shifted off. If I convert 2550 to binary, and then find the next
largest binary number with alternating 1s and 0s, then that ought to be the
solution.

2550 in binary is  : 1001 1111 0110
Next largest number: 1010 1010 1010 ==> 2730

The register 'a' should be set to: 2730 - 2550 => 180.