# Jacobian Matrix

Advanced | calculus

### The problem, from first principles

`02-partial-derivatives`'s gradient answers "how does one number (a loss) respond to changes in many inputs." But most operations in a real network don't collapse down to one number, `linear` alone maps `in_features` inputs to `out_features` outputs, every one of which can respond differently to a nudge in any given input. You need the gradient's generalization: not one row of sensitivities, but a whole grid of them, one row per output, one column per input.

That grid is the Jacobian, and it is the object every "vector-in, vector-out" operation's backward pass is secretly built on top of, even though, as you'll see in the Autograd track, real backward passes are clever enough to never form the whole matrix explicitly.

### From theory to code

Theory generalizes `02-partial-derivatives`'s single-output gradient to many outputs at once: row `i` is output `i`'s own gradient. Implement it by evaluating `f` once to learn the output size, then, for each input coordinate, applying the central difference to the ENTIRE output vector simultaneously, filling in one column of the result per input coordinate.

Implement `jacobian(f, x, eps=1e-5)` against that reasoning. The signature and docstring are already in the editor.

### Constraints

- `f` takes a length-`n` vector and returns a length-`m` vector, or a scalar (treated as `m = 1`).
- Use `np.atleast_1d` on `f`'s output so both cases are handled uniformly.
- Result shape is always `(m, n)`: `m` rows (one per output), `n` columns (one per input).

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

Call `f(x)` once, before the main loop, purely to learn `m` via `len(np.atleast_1d(f(x)))`. You'll then call `f` again inside the loop for the actual finite differences.

</details>

<details>
<summary>Hint 2</summary>

The loop is over input coordinates `j`, not output coordinates. Each iteration fills one entire COLUMN of the result, `result[:, j]`, using the same central-difference formula applied to a vector-valued `f` instead of a scalar one.

</details>
