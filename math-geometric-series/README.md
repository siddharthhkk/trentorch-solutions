# Geometric Series

Beginner | calculus | series

### The problem, from first principles

A geometric series adds up a list of numbers where each one is the previous one multiplied by the same fixed ratio: a bank balance that grows by 5% every year, a signal that loses half its strength at every step, a reward that is worth a little less with each step of delay. Adding the terms one by one works for a few terms, but it gives no way to answer the questions that matter: what is the total after a million terms, and does the total settle on a finite number if the list never ends? This question builds the closed forms that answer both.

### From theory to code

Implement `geometric_partial_sum(a, r, n)`, the sum of the first `n` terms, then `geometric_series_sum(a, r)`, the sum of the infinite series when it has one, then `terms_needed(a, r, tolerance)`, how many terms are needed before the partial sum is within `tolerance` of the infinite sum. The signatures and docstrings are already in the editor.

### Constraints

- `a` is the first term and `r` is the common ratio, both floats. The series is `a + a*r + a*r**2 + ...`.
- `geometric_partial_sum` takes an integer `n >= 0`. With `n = 0` there are no terms, so the sum is `0.0`. It must handle `r == 1` without dividing by zero, and it must not loop over the terms.
- `geometric_series_sum` only exists when `|r| < 1`. For any other ratio it raises `ValueError`.
- `terms_needed` requires `|r| < 1` and `tolerance > 0`, and returns the smallest integer `n >= 0` such that the gap between the infinite sum and the sum of the first `n` terms is below `tolerance`. If `a == 0` the answer is `0`.

### Hints

<details>
<summary>Hint 1</summary>

Multiply the partial sum by `r` and subtract it from the original. Almost every term cancels and a closed form is left, with `1 - r` in the denominator. That is also why `r == 1` needs its own case.

</details>

<details>
<summary>Hint 2</summary>

The gap between the infinite sum and the first `n` terms is the tail, which is itself a geometric series that starts at `a * r**n`. Its size has a closed form, so you can solve for `n` with a logarithm instead of testing values one at a time.

</details>
