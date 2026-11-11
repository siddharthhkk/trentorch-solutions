# Confidence Intervals

Intermediate | probability

### The problem, from first principles

`07-likelihood-estimation`'s `mle_normal_mean` gives you ONE number, the sample mean, as your best guess at the true population mean. But a single number hides an important fact: that guess is uncertain, a different sample of the same size would almost certainly give a slightly different mean. A confidence interval makes that uncertainty explicit: instead of "the average is 100," it says "the average is likely somewhere between 94 and 106," a genuinely more honest and more useful statement, especially when a decision hinges on how confident you actually are.

This is the tool that turns "here's a number" into "here's a number, and here's how much I'd trust it," essential whenever a sample is small, or a decision (does this new feature actually help users? is this new drug better?) needs to account for the possibility that an observed difference is just sampling noise.

### From theory to code

Theory needs the standard error of the mean (how much sample means themselves vary) and a critical value from the t-distribution (which correctly widens the interval for small samples, where a plain Normal approximation would be overconfident).

Implement `standard_error_of_mean(x)` first, then `confidence_interval_mean(x, confidence=0.95)` on top of it.

### Constraints

- `standard_error_of_mean` uses `ddof=1` (the unbiased/Bessel-corrected std), `05-expectation-covariance`'s convention for estimating from a sample.
- `confidence_interval_mean` uses the t-distribution (the provided `_t_ppf`, an exact `scipy.stats.t.ppf`-equivalent built from `numpy`/`math` alone), not a fixed z-value, so it stays valid for any sample size.
- Returns a `(lower, upper)` tuple.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`standard_error_of_mean` is `np.std(x, ddof=1) / np.sqrt(len(x))`, one line.

</details>

<details>
<summary>Hint 2</summary>

`stats.t.ppf((1 + confidence) / 2, df=len(x) - 1)` gives the t-distribution's critical value for a two-sided interval at the requested confidence level.

</details>
