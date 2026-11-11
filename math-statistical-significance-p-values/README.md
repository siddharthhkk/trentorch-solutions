# Significance & p-Values

Beginner | probability

### The problem, from first principles

`03-hypothesis-testing` and `04-ab-testing` both produce a p-value and a conventional cutoff, `p < 0.05`, is called "statistically significant." This question tackles the part of the picture those two questions left implicit and dangerously easy to misuse: what does `alpha = 0.05` actually promise, and what happens the moment you run more than one test?

The genuinely important, often-missed fact: `alpha = 0.05` means "a 5% chance of a FALSE POSITIVE on any single test where the null hypothesis is actually true." Run 100 such tests, and even if NOTHING real is going on anywhere, you'd still expect roughly 5 of them to falsely come back "significant," purely from chance. Testing dozens of features against a target, or running dozens of A/B test variants, and reporting only the "significant" ones without accounting for this, is one of the most common, genuinely misleading statistical mistakes in practice.

### From theory to code

Theory defines the significance threshold directly, and derives two consequences of running multiple tests: how many false positives to expect by chance alone, and a simple correction (Bonferroni) that keeps the overall false-positive rate under control.

Implement `is_statistically_significant(p_value, alpha=0.05)`, `expected_false_positives(num_tests, alpha=0.05)`, and `bonferroni_corrected_alpha(num_tests, alpha=0.05)` against that reasoning.

### Constraints

- `is_statistically_significant` is a strict `<` comparison, not `<=`.
- `expected_false_positives` and `bonferroni_corrected_alpha` are direct, one-line formulas, no simulation needed inside the functions themselves.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`expected_false_positives` is exactly `num_tests * alpha`, the expected count under "every null hypothesis is true."

</details>

<details>
<summary>Hint 2</summary>

`bonferroni_corrected_alpha` divides the original alpha by the number of tests, a stricter per-test bar that keeps the COMBINED false-positive rate near the original alpha.

</details>
