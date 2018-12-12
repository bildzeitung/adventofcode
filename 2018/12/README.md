Part 2:
=======

For Part 2, I submitted an analytical solution. The rules are such that the
input ends up with a fixed string that slides to the right, which means that
the total is a fixed increment per generation after some point.

For the test input, that was generation *159*, and the delta between
generations was *33*. The total at generation *159* was *5302*.

The final answer, then, is:
  `5302 + 33 * (50_000_000_000 - 159)
