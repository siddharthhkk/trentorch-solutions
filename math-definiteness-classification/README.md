# Classifying Definiteness

Advanced | linear-algebra | matrices | optimization

### The problem, from first principles

The questions before this one each asked a yes-or-no about one kind of matrix: positive definite, positive semi-definite, negative definite, negative semi-definite. A symmetric matrix actually falls into exactly one of five classes, and the fifth is the one that causes trouble in optimization: a matrix that curves up in some directions and down in others, the shape of a mountain pass. Knowing which class the Hessian at a critical point belongs to is what tells you whether you have found a minimum, a maximum or a saddle. This question puts all five together and adds a second test, Sylvester's criterion, that decides positive definiteness from determinants alone.

### From theory to code

Implement `leading_principal_minors(a)`, the determinants of the top-left squares of a matrix, then `is_positive_definite_sylvester(a)`, which decides positive definiteness from them, then `classify_definiteness(a, tol)`, which names the class of a symmetric matrix, then `critical_point_type(hessian, tol)`, which turns that class into a verdict about a critical point. The signatures and docstrings are already in the editor.

### Constraints

- `leading_principal_minors(a)` takes a square `n x n` array and returns a 1D array of length `n` whose entry `k - 1` is the determinant of the top-left `k x k` block.
- `is_positive_definite_sylvester(a)` returns `True` only for a square symmetric matrix whose leading principal minors are all strictly positive. It must not compute eigenvalues.
- `classify_definiteness(a, tol)` requires a square symmetric matrix and raises `ValueError` otherwise. It returns exactly one of the strings `"positive definite"`, `"positive semidefinite"`, `"negative definite"`, `"negative semidefinite"`, `"indefinite"` or `"zero"`. An eigenvalue within `tol` of zero counts as zero, and `"zero"` is returned only when every eigenvalue is within `tol` of zero.
- `critical_point_type(hessian, tol)` returns `"local minimum"` for positive definite, `"local maximum"` for negative definite, `"saddle point"` for indefinite, and `"inconclusive"` for the semidefinite and zero cases. It raises `ValueError` for a non-symmetric Hessian.

### Hints

<details>
<summary>Hint 1</summary>

Count how many eigenvalues are clearly positive, clearly negative and within `tol` of zero. The class is a function of those three counts and nothing else.

</details>

<details>
<summary>Hint 2</summary>

Sylvester's criterion tests the determinants of the growing top-left squares. A single number that is not strictly positive anywhere in that list rules out positive definiteness.

</details>

<details>
<summary>Hint 3</summary>

Second-order information only decides the case when the curvature is nonzero in every direction. A semidefinite Hessian has a direction with zero curvature, so the second-order test cannot say more.

</details>
