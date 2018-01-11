# Solution notes for Part 2

To solve, there's the possiblity of
    (a) re-writing the assembunny to accomodate a multiply instruction
        (that is, an optimisation of the VM & program)
    (b) figure out what the program does and solve for a = 12

I chose (b). The 2.py contains a debugger implementation, however, to help
expedite the analysis.

Given that register 'a' is the only one set, this is a function of one
variable, so f(a) = ? is the question we need to answer.

Breaking the program down roughly, we have:
* 2-12 calculate a = a * b, where b = a - 1
* 11-15 calculate b--, c = b * 2
* once b is less than 5, it starts to toggle instructions
* until then, instruction 18 jumps back to the 2-12 block
* when b = 1, the jnz is toggled and the loop ends; the result is that
  a = a! (vis a vis, a = a * (a-1) * (a-2) * .. * 3 * 2)
* the final block, which has been toggled a bit, adds a fixed constant
  to a.
* From instructions 19 and 20, a += 97 * 79

Thus, f(a) <- a! + 7663. 