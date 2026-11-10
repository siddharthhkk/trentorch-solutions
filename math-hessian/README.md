# Hessian Matrix

Advanced | calculus | optimization

### The problem, from first principles

A gradient of zero tells you a function is momentarily flat, but flat could mean you're at the bottom of a bowl (great, you're done), the top of a hill (terrible, you want to be anywhere else), or on a mountain pass that's flat in one direction and steeply curved in another (a saddle, training can get stuck circling one of these). The gradient alone genuinely cannot distinguish these three situations, it only knows "flat right here," not "which way does flat curve."

The Hessian is the tool that answers "which way does it curve": the full matrix of second derivatives, one entry for every pair of input coordinates. And, as `08-positive-definite-matrices` already set up, its eigenvalues turn that matrix into a clean, three-way answer.

### From theory to code

Theory frames the Hessian as literally the Jacobian of the gradient, which means you already have every piece needed to build it: `04-jacobian`'s central-difference-over-a-vector-valued-function structure, applied to `gradient` (from `02-partial-derivatives`) instead of to `f` directly. Implement that, then use `08-positive-definite-matrices`'s eigenvalue-sign logic to classify a critical point.

Implement `hessian(f, x, eps=1e-4)` and `classify_critical_point(hessian_matrix)` against that reasoning. The signatures and docstrings are already in the editor.

### Constraints

- `f` is scalar-valued (`R^n -> R`), `hessian`'s result is always `(n, n)`.
- Use the provided `gradient` (imported at the top of the file) as the thing you're differentiating, don't call `f` directly inside `hessian`.
- `classify_critical_point` must use a small tolerance around zero when checking eigenvalue signs, not a bare `> 0`/`< 0`.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

The Hessian is the Jacobian of the gradient. If you already understand `04-jacobian`, you already understand the loop structure this question needs, just swap which function is being differentiated.

</details>

<details>
<summary>Hint 2</summary>

`np.linalg.eigvalsh` (from `06-eigenvalues-eigenvectors`/`08-positive-definite-matrices`) gives you the eigenvalues directly. Check whether every one is comfortably positive, comfortably negative, or neither.

</details>
