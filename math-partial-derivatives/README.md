# Partial Derivatives

Beginner | calculus

### The problem, from first principles

A single-variable derivative answers "how does output change as this one input changes." But a real loss function depends on hundreds, thousands, or millions of numbers at once, every weight and bias in a network. You can't ask "how does the loss change" without saying _which_ number you're wiggling, so the natural move is to ask the single-variable question over and over, once per number, holding everything else perfectly still each time.

That's a partial derivative. And collecting every one of those answers into a single vector, one entry per parameter, gives you the gradient, the object every optimizer in this curriculum (`04-gd-step` onward) actually steps against.

### From theory to code

Theory reduces a partial derivative to `01-derivatives-first-principles`'s central difference, applied to just one coordinate of a multi-dimensional input while every other coordinate stays fixed. Implement that first, then collect it across every coordinate to build the full gradient.

Implement `partial_derivative(f, x, index, eps=1e-5)` and `gradient(f, x, eps=1e-5)` against that reasoning. The signatures and docstrings are already in the editor.

### Constraints

- `f` takes a NumPy array `x` and returns a scalar.
- `partial_derivative` must not mutate the caller's `x`, copy before nudging.
- `gradient`'s output has the same shape as `x`, one partial derivative per coordinate, in the same order.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`x.copy()` before nudging a single coordinate. Mutating the array a caller handed you is a silent bug waiting to happen.

</details>

<details>
<summary>Hint 2</summary>

`gradient` is a one-line loop (or list comprehension) calling `partial_derivative` once per index, it does no numerical work of its own.

</details>
