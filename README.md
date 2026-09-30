# Cryptography Maths Toolkit

A menu based Python learning project adapted from Applied Cryptography Seminar 6. It explores the mathematics behind public-key cryptography through small examples.

## Features

- Modular addition and subtraction.
- Modular exponentiation using `pow(message, exponent, modulus)`.
- Modular inverses using the Extended Euclidean Algorithm.
- Prime checks using trial division.
- Counting points on a small elliptic curve, including the point at infinity.

## Run

Requires Python 3.9 or newer. No extra packages are needed.

```bash
python3 maths_toolkit.py
```

On Windows, use `python maths_toolkit.py` if needed. Choose a menu option, enter the requested integers and use `0` to exit.

In Carnets, put the file in the notebook's working folder and try:

```python
%run maths_toolkit.py
```

The revised version was tested with Python, but not in the Carnets app.

## Seminar answers and examples

| Calculation | Answer | Check or explanation |
|---|---|---|
| `(963 + 842) mod 79` | 67 | `1805 = 79 × 22 + 67` |
| `(6 - 4) mod 9` | 2 | Modular subtraction |
| `7^4 mod 35` | 21 | `pow(7, 4, 35)` |
| Inverse of 23 modulo 899 | 430 | `23 × 430 = 899 × 11 + 1` |
| A residue with no inverse modulo 899 | 29 | `899 = 29 × 31`, so they share a factor |
| Is 899 prime? | No | It factors as `29 × 31` |
| Points on `y² = x³ + x + 1 mod 5` | 9 | Eight finite points and the point at infinity |

## How it works

The `%` operator gives a remainder. A modular inverse of `a` is a number `x` such that `(a * x) % n == 1`. An inverse exists exactly when `a` and `n` are coprime.

The Extended Euclidean Algorithm calculates the greatest common divisor and coefficients satisfying `a*x + n*y = gcd(a,n)`. When the gcd is 1, reducing `x` modulo `n` gives the inverse.

The three-argument `pow()` computes modular exponentiation efficiently without constructing the full integer power first. This demonstrates the mathematical RSA operation; it does not implement RSA key generation or encryption padding.

For elliptic curves, the program counts square residues once, then checks each x-coordinate. That avoids the original nested loop over all possible pairs. It includes the point at infinity. It rejects singular curves and limits the exercise to prime moduli greater than 3 and at most 10000.

The expression `4*a³ + 27*b²` must be nonzero modulo the prime for this short Weierstrass model. It differs from the full curve discriminant by a nonzero factor when the prime is greater than 3, so it gives the required zero/nonzero check in this setting.

## Limits

These are teaching tools for small inputs. Trial division is not suitable for generating real RSA primes. Counting curve points is not an implementation of elliptic-curve encryption. The interactive prime check limits inputs to an absolute value of 10000000 to keep the examples manageable.

## Skills demonstrated

Python functions, loops, validation, modular arithmetic, algorithms, mathematical reasoning and comparison against a simpler reference calculation.

## Attribution

Original exercises and starter algorithms: university Applied Cryptography Seminar 6. Extensions include subtraction, modular exponentiation, iterative Euclidean calculation, input validation and an improved point counting implementation.

## References

- [Python built-in pow documentation](https://docs.python.org/3/library/functions.html#pow)
- [SageMath elliptic curves](https://doc.sagemath.org/html/en/reference/arithmetic_curves/)
- Applied Cryptography Seminar 6 materials supplied with the exercise.

