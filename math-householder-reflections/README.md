# Householder Reflections

Intermediate | linear-algebra | orthogonalization

### The problem, from first principles

`01-gram-schmidt` builds an orthonormal basis by subtracting projections one vector at a time, which is easy to follow but loses accuracy when the input vectors are nearly parallel. A Householder reflection takes a different route to the same goal. It is a single mirror: pick a direction, and flip every vector across the plane perpendicular to it. With the right choice of direction, one mirror swings any chosen vector onto an axis, wiping out all of its entries except the first. Chaining a few such mirrors is how numerical libraries orthogonalize in practice. This question builds the mirror itself.

### From theory to code

Implement `householder_vector(x)`, which finds the mirror direction that sends `x` onto the first axis, `householder_matrix(v)`, which builds the full reflection matrix for a direction, and `apply_householder(v, a)`, which applies the reflection to a vector or a matrix without ever forming the matrix. The signatures and docstrings are already in the editor.

### Constraints

- `x` is a 1D array of floats. `householder_vector` returns a 1D array `v` of the same length such that reflecting `x` across the plane perpendicular to `v` gives `-sign(x[0]) * norm(x)` in the first entry and zeros elsewhere. Use `sign(0) = 1`.
- If `x` is the zero vector, return the zero vector. The reflection built from a zero direction is the identity.
- `householder_matrix(v)` returns the `n x n` matrix `I - 2 v v^T / (v^T v)`. For a zero `v` it returns the identity.
- `apply_householder(v, a)` returns the reflection of `a` for `a` a 1D vector or a 2D matrix (reflecting each column). It must not build the `n x n` reflection matrix and must not change `v` or `a`.

### Hints

<details>
<summary>Hint 1</summary>

The mirror that sends `x` to a multiple of `e1` has a direction along `x - alpha * e1`, where `alpha` is the target value. Both signs of `alpha` work in exact arithmetic, but one of them subtracts two nearly equal numbers when `x` is already close to the first axis. Choose the sign so the first entry of `v` gets larger in size, not smaller.

</details>

<details>
<summary>Hint 2</summary>

Reflecting `a` across the plane perpendicular to `v` is `a - 2 * v * (v @ a) / (v @ v)`. The product `v @ a` is one number for a vector and one number per column for a matrix, so the same line covers both cases.

</details>
