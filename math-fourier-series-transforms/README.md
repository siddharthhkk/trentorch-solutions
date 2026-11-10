# Fourier Series & Transforms

Advanced | calculus | series | signals

### The problem, from first principles

`02-taylor` approximates a function near one point by adding up powers of `x - a`. Fourier analysis approximates a function over a whole stretch by adding up waves instead: a repeating signal, however jagged, can be written as a sum of sines and cosines whose frequencies are whole multiples of a base frequency. The transform that finds those waves, and the inverse that rebuilds the signal from them, are among the most used algorithms in computing. This question builds both from their definitions, for a continuous periodic function (the series) and for a list of samples (the discrete transform).

### From theory to code

Implement `fourier_coefficients(f, period, num_terms, num_samples)` to find the cosine and sine weights of a periodic function, `fourier_series_eval(a0, a, b, period, t)` to rebuild the function from them, then `dft(x)` and `inverse_dft(spectrum)` for the discrete transform of a sample list, and `dominant_frequency(x, sample_rate)` to read the strongest frequency out of a signal. The signatures and docstrings are already in the editor.

### Constraints

- `f` takes a NumPy array of times and returns an array of the same shape. It repeats every `period`.
- `fourier_coefficients` estimates the integrals by averaging `f` at `num_samples` evenly spaced times over one period, starting at `t = 0`. It returns `(a0, a, b)` where `a` and `b` are arrays of length `num_terms` holding the weights for harmonics `1` through `num_terms`. The series is `a0 / 2 + sum(a[k-1] * cos(2*pi*k*t/period) + b[k-1] * sin(2*pi*k*t/period))`.
- `fourier_series_eval` accepts `t` as a float or an array and returns the same shape.
- `dft` and `inverse_dft` use the definition directly with a matrix of complex exponentials. They must not call `np.fft`. `dft` takes a 1D array of length `N` and returns a complex array of length `N`. `inverse_dft` returns a complex array that is the exact inverse.
- `dominant_frequency` returns the frequency in Hz of the largest-magnitude bin among frequencies from 1 bin up to the Nyquist bin, ignoring the zero-frequency (average) bin. `sample_rate` is in samples per second.

### Hints

<details>
<summary>Hint 1</summary>

Each weight is an average of `f(t)` multiplied by a cosine or sine of the matching frequency, times 2. Averaging over evenly spaced samples of one full period is the numerical stand-in for the integral.

</details>

<details>
<summary>Hint 2</summary>

Build the transform as one matrix: entry `(k, n)` is `exp(-2j * pi * k * n / N)`. Then `dft(x)` is a matrix-vector product, and the inverse uses the conjugate of the same matrix divided by `N`.

</details>

<details>
<summary>Hint 3</summary>

Bin `k` of an `N`-sample transform corresponds to a frequency of `k * sample_rate / N`. Only bins up to `N // 2` are independent for a real signal, since the rest mirror them.

</details>
