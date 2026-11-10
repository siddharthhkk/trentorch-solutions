# Directional Derivatives

Intermediate | calculus | optimization

### The problem, from first principles

Standing on a hillside, "how steep is it here" isn't a complete question, steepness depends entirely on which way you're facing. Walk along a contour line and it's flat; walk straight up the slope and it's as steep as it gets. `02-partial-derivatives` only ever asked about steepness along the coordinate axes (due east, due north). This question asks the more general version: how steep is it in ANY direction you choose, and, crucially, which single direction is steepest of all.

That "which direction is steepest" answer turns out to be the gradient itself, not just a bookkeeping vector of per-axis sensitivities but a genuine compass pointing the way uphill fastest. This is the fact that makes gradient descent (`04-gd-step`) actually work: stepping opposite the gradient isn't an arbitrary heuristic, it's stepping in the single most effective downhill direction available.

### From theory to code

Theory shows a directional derivative is just `01-derivatives-first-principles`'s central difference, evaluated by stepping along an arbitrary unit vector instead of a coordinate axis, and that the gradient, normalized to unit length, IS the direction of steepest increase. Implement both directly, reusing `02-partial-derivatives`'s `gradient` for the second one.

Implement `directional_derivative(f, x, direction, eps=1e-5)` and `steepest_ascent_direction(f, x)` against that reasoning. The signatures and docstrings are already in the editor.

### Constraints

- `direction` is not guaranteed to already be a unit vector, normalize it first.
- `steepest_ascent_direction` returns a unit vector (norm 1), pointing in the gradient's direction, not the raw gradient itself.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`direction / np.linalg.norm(direction)` turns any nonzero vector into a unit vector pointing the same way.

</details>

<details>
<summary>Hint 2</summary>

`steepest_ascent_direction` needs no new numerical machinery: compute the gradient, then normalize it the same way you normalized `direction` above.

</details>
