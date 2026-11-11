# Cross-Entropy

Intermediate | information-theory

### The problem, from first principles

`01-entropy` measured "how surprising is this distribution, to someone who already knows it exactly." Cross-entropy asks a subtly different, far more practically important question: "how surprising is the TRUE distribution, to someone whose beliefs are only an approximation of it?" That someone-with-imperfect-beliefs is exactly what a trained classifier is: it outputs a predicted probability for each class, and the true label (a one-hot distribution, all probability on the correct class) is what actually happened. Cross-entropy measures how many bits of surprise the model's imperfect beliefs cost you, on average, versus if you'd known the truth exactly.

This is not a coincidence of naming: `02-cross-entropy` (Deep Learning Core) IS this exact quantity, computed between a one-hot true label and a softmax-predicted distribution, this question builds the general concept first so that formula stops looking like an arbitrary loss and starts looking like the specific, principled thing it actually is.

### From theory to code

Theory changes exactly one thing from `01-entropy`'s formula: the log is taken of the PREDICTED distribution `q`, while the outer weighting is still by the TRUE distribution `p`. Implement that directly.

Implement `cross_entropy(p, q, base=2.0)` against that reasoning. The signature and docstring are already in the editor.

### Constraints

- `p` and `q` are both valid probability distributions over the same set of outcomes.
- Clip `q` (not `p`) before taking its log, for the same `log(0)` reason `01-entropy` clips.
- `cross_entropy(p, p, base)` must equal `01-entropy`'s `entropy(p, base)` exactly, they're the same formula when `p == q`.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

Copy `01-entropy`'s formula and change exactly one variable name inside the `log(...)` call.

</details>

<details>
<summary>Hint 2</summary>

The outer multiplying factor stays `p` (the true weighting of outcomes), only the argument to `log` changes to `q` (the predicted probability of that outcome).

</details>
