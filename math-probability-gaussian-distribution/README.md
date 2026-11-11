# Gaussian Distribution

Intermediate | probability | distributions

### The problem, from first principles

Most naturally occurring measurement noise, sensor error, rounding error, the sum of many small independent effects, piles up into the same recognizable shape: symmetric, peaked at the average, thinning out fast at the extremes. That shape is the Gaussian, and it is not a coincidence it shows up everywhere; the Central Limit Theorem explains exactly why.

Here you'll implement the Gaussian's probability density function directly from its formula, then generate actual Gaussian-distributed samples from nothing but uniform random numbers using the **Box-Muller transform**, the concrete answer to "where does randomness with this specific shape actually come from."

### From theory to code

Implement `gaussian_pdf(x, mu, sigma)` against the closed-form density in Theory, then `sample_gaussian(mu, sigma, n, uniform_draws)`, which turns pairs of uniform random draws into Gaussian samples via Box-Muller. The signatures and docstrings are already in the editor.

### Constraints

- `sigma > 0` (a zero or negative standard deviation is undefined).
- `x` may be a scalar or a NumPy array of any shape.
- `uniform_draws` are pre-generated floats in `[0, 1)`, exactly `2 * n` of them, so results are deterministic and checkable.
- Return samples as a flat array of length `n`.

### Hints

<details>
<summary>Hint 1</summary>

Box-Muller turns _two_ uniform draws `u1, u2` into _two_ independent standard-normal samples at once, you'll use `n/2` pairs (rounded up) to get `n` samples.

</details>

<details>
<summary>Hint 2</summary>

A standard-normal sample `z` (μ=0, σ=1) becomes a general Gaussian sample via `x = mu + sigma * z`, generate standard-normal first, then shift/scale.

</details>
