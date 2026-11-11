# KL Divergence

Intermediate | information-theory

### The problem, from first principles

`02-cross-entropy`'s Gibbs' inequality guarantees `H(p, q) >= H(p)`, cross-entropy is never smaller than the true distribution's own entropy. But it left one question unanswered: exactly HOW MUCH bigger is it? That gap, cross-entropy minus true entropy, is a distribution's own unavoidable baseline surprise subtracted out, isolates exactly the extra cost caused by `q` being a wrong (or imperfect) approximation of `p`. That gap is KL divergence, and unlike cross-entropy, it's zero precisely when the approximation is perfect, making it a genuine (if asymmetric) measure of "distance" between two distributions.

This measures the exact quantity model distillation minimizes (how far is a smaller "student" model's predicted distribution from a larger "teacher" model's), and it's the quantity variational inference and diffusion models are built on, both outside this curriculum's main path, but both direct extensions of the exact formula this question implements.

### From theory to code

Theory defines KL divergence as literally `cross_entropy(p, q) - entropy(p)`, the gap Gibbs' inequality guarantees is non-negative. Implement it as that one-line combination of the two functions you've already built.

Implement `kl_divergence(p, q, base=2.0)` against that reasoning. The signature and docstring are already in the editor.

### Constraints

- `kl_divergence(p, p, base)` must equal `0.0` (up to floating-point tolerance) for any valid distribution `p`.
- `kl_divergence` must never be negative.
- Reuse `entropy` and `cross_entropy` directly (both already imported at the top of the file), don't reimplement either formula.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

This is a one-line function: `cross_entropy(p, q, base) - entropy(p, base)`.

</details>

<details>
<summary>Hint 2</summary>

If your result isn't exactly `0.0` when `p == q`, double check you passed the SAME `base` to both `cross_entropy` and `entropy`.

</details>
