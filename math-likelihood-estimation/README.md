# Likelihood & Estimation

Advanced | probability

### The problem, from first principles

**Likelihood vs probability**

"Given a fair coin, what's the chance of seeing 8 heads in 10 flips" and "given that I saw 8 heads in 10 flips, how fair was the coin" use the exact same binomial formula, plugged in two different ways. The first fixes the coin's fairness and asks about possible outcomes, that's a probability. The second fixes the outcome (it already happened) and asks about possible explanations, that's a likelihood. Same formula, same numbers even, but a completely different question being asked of it, and confusing the two is a genuinely common source of statistical mistakes.

This distinction underlies every "fit a model to data" question this curriculum poses: maximum likelihood estimation (the next question in this track) is precisely "find the parameter values that make the DATA YOU ACTUALLY OBSERVED look as likely as possible," which only makes sense once you've separated "probability of data, given parameters" from "likelihood of parameters, given data."

**Maximum likelihood**

`07-likelihood-estimation`'s `likelihood_curve` swept a grid of candidate means and evaluated each one, then you could squint at a plot and guess where the peak was. That's fine for one parameter and a hand-picked grid, but it doesn't scale, doesn't give an exact answer, and doesn't generalize to distributions with several parameters at once (mean AND std together).

Maximum likelihood estimation (MLE) is the principled version of "find where the likelihood curve peaks": instead of searching a grid, use calculus, set the derivative of the (log-)likelihood to zero and solve, to get an exact, closed-form answer directly. For a Normal distribution, this turns out to have a remarkably simple, familiar answer.

**MAP estimation**

`07-likelihood-estimation`'s MLE has a real weakness: with very little data, it trusts that small sample completely, 3 coin flips landing heads twice gives an MLE of 66.7% heads, even though you might have good reason to believe, before seeing any flips, that most coins are close to fair. MLE has no way to incorporate that prior belief, it only ever looks at the data in front of it.

MAP (Maximum A Posteriori) estimation fixes exactly this: it combines the likelihood (how well a parameter explains the data, MLE's whole criterion) with a prior (`04-conditional-bayes`'s prior belief, before seeing the data), and finds the parameter value that maximizes their product, the posterior. With a very informative prior and little data, MAP leans on the prior; with lots of data, MAP converges to the same answer MLE would give, the data eventually overwhelms any reasonable prior.

### From theory to code

**Likelihood vs probability**

Theory defines the Normal PDF once, then uses it two different ways: as a probability density over data (fixed parameters, varying data), and as a likelihood over parameters (fixed data, varying parameters). Implement the PDF once, a joint-density helper for a fixed parameter, and a likelihood curve that sweeps candidate parameter values against the SAME fixed data.

Implement `normal_pdf(x, mean, std)`, `joint_density(x_values, mean, std)` and `likelihood_curve(x_values, candidate_means, std)` against that reasoning. The signatures and docstrings are already in the editor.

**Maximum likelihood**

Theory works in log-space (summing log-densities rather than multiplying raw densities, for numerical stability) and derives closed-form MLE formulas for a Normal distribution's mean and standard deviation by setting derivatives to zero. Implement the log-space objective first (so you can numerically verify the closed forms against it), then the two closed-form estimators directly.

Implement `negative_log_likelihood_normal(x, mean, std)`, `mle_normal_mean(x)` and `mle_normal_std(x)` against that reasoning. The signatures and docstrings are already in the editor.

**MAP estimation**

Theory expresses the (unnormalized) log-posterior as the log-likelihood plus the log-prior, and, for the specific case of a Normal likelihood with a Normal prior on the mean, derives a closed-form MAP estimate: a precision-weighted average of the sample mean and the prior mean.

Implement `negative_log_posterior_normal(mean_candidate, x, data_std, prior_mean, prior_std)` (reusing `07-likelihood-estimation`'s NLL and `07-likelihood-estimation`'s `normal_pdf`), then `map_estimate_normal_mean(x, data_std, prior_mean, prior_std)`, the closed form.

### Constraints

**Likelihood vs probability**

- `normal_pdf` must vectorize over `x` (accept an array, return an array of the same shape).
- `joint_density` assumes every entry of `x_values` is independent, so their joint density is a product, not a sum.
- `likelihood_curve` calls `joint_density` once per candidate mean, holding `x_values` and `std` fixed throughout.

**Maximum likelihood**

- `negative_log_likelihood_normal` works in log-space (sum of `log(density)`), not `-log(product of densities)`.
- `mle_normal_mean` and `mle_normal_std` are closed-form (no search, no calls to `negative_log_likelihood_normal`).
- `mle_normal_std` divides by `n` (the biased estimator), not `n - 1`, Theory explains why MLE gives this specific version.

**MAP estimation**

- `data_std` is assumed known and fixed, only the mean is being estimated.
- `map_estimate_normal_mean` is closed-form, no search.
- With a very large `prior_std` (an uninformative prior), the MAP estimate should approach the plain sample mean (MLE).
- With a very small `prior_std` (an extremely confident prior), the MAP estimate should approach `prior_mean` itself.

### Hints

**Likelihood vs probability**

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`normal_pdf` is a direct, vectorized translation of the Gaussian formula, `np.exp` and `np.sqrt` handle arrays natively.

</details>

<details>
<summary>Hint 2</summary>

`joint_density` is `np.prod(normal_pdf(x_values, mean, std))`, one call reusing the function you already wrote.

</details>

**Maximum likelihood**

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`log(a * b * c) = log(a) + log(b) + log(c)`. Turn the product from `joint_density` into a sum of logs instead.

</details>

<details>
<summary>Hint 2</summary>

The MLE for the mean of a Normal distribution turns out to be exactly the plain sample average, no surprise formula needed.

</details>

**MAP estimation**

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`negative_log_posterior_normal` is a sum of two pieces you already have: the NLL of the data under `mean_candidate`, and the negative log of the prior's density AT `mean_candidate`.

</details>

<details>
<summary>Hint 2</summary>

"Precision" is `1 / variance`. The MAP mean is `(data_precision * sample_mean + prior_precision * prior_mean) / (data_precision + prior_precision)`, a weighted average where more precision (less variance, more confidence) means more weight.

</details>
