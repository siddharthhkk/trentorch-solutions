# A/B Testing

Intermediate | probability

### The problem, from first principles

A website shows 1,000 visitors the old checkout button, 120 buy. It shows 1,000 different visitors a new button design, 150 buy. Is the new design genuinely better, or would two random 1,000-visitor samples from a page with NO real change plausibly land 30 conversions apart just from chance? This is the exact question `03-hypothesis-testing` answered for continuous measurements (like page-load times); A/B testing is the same question, specialized to CONVERSION RATES, proportions, not continuous numbers, which needs a slightly different formula.

This is quite possibly the single most common real-world application of statistical hypothesis testing: nearly every product decision informed by data ("did the new feature increase signups," "did the redesign hurt checkout completion") ultimately reduces to exactly this comparison.

### From theory to code

Theory pools both groups' conversion counts into one combined rate (the correct approach under the assumption both groups truly share the same underlying rate, the null hypothesis being tested), uses it to compute a standard error, and converts the observed gap into a z-statistic and two-sided p-value.

Implement `conversion_rate(conversions, visitors)` first, then `two_proportion_z_test(conversions_a, visitors_a, conversions_b, visitors_b)` on top of it.

### Constraints

- Uses the POOLED proportion (combining both groups) for the standard error, not each group's own rate separately.
- Returns a two-sided `(z_statistic, p_value)` pair.
- Computes the two-sided p-value with `math.erfc(abs(z_statistic) / math.sqrt(2.0))`, avoiding cancellation error when the p-value is extremely small.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`p_pooled = (conversions_a + conversions_b) / (visitors_a + visitors_b)`, treating both groups as one combined sample for the purpose of estimating the shared rate under the null hypothesis.

</details>

<details>
<summary>Hint 2</summary>

The standard error uses the pooled proportion twice: `sqrt(p_pooled * (1 - p_pooled) * (1/visitors_a + 1/visitors_b))`.

</details>
