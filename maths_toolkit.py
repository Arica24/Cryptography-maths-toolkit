"""Small educational mathematical tools adapted from Cryptography Seminar 6."""
from collections import Counter


def validate_modulus(n):
    if n <= 1:
        raise ValueError('Modulus must be an integer greater than 1.')


def mod_add(a, b, n):
    validate_modulus(n)
    return (a + b) % n


def mod_subtract(a, b, n):
    validate_modulus(n)
    return (a - b) % n


def modular_power(message, exponent, n):
    validate_modulus(n)
    if exponent < 0:
        raise ValueError('Use a non-negative exponent for this demonstration.')
    return pow(message, exponent, n)


def extended_gcd(a, b):
    """Iterative Euclidean algorithm: return gcd and Bezout coefficients."""
    old_r, r = a, b
    old_x, x = 1, 0
    old_y, y = 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y
    if old_r < 0:
        return -old_r, -old_x, -old_y
    return old_r, old_x, old_y


def mod_inverse(a, n):
    validate_modulus(n)
    gcd, x, _ = extended_gcd(a, n)
    return x % n if gcd == 1 else None


def is_prime(n):
    """Trial division for small learning examples, not cryptographic key generation."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def count_curve_points(a, b, p):
    # This short Weierstrass demonstration is limited to small primes > 3.
    if p <= 3 or p > 10000 or not is_prime(p):
        raise ValueError('Choose a prime between 5 and 10000 for this small-field demo.')
    if (4 * pow(a, 3, p) + 27 * pow(b, 2, p)) % p == 0:
        raise ValueError('This curve is singular; choose different coefficients.')
    # Count square residues once, avoiding a nested loop over every (x, y).
    square_counts = Counter((y * y) % p for y in range(p))
    return 1 + sum(square_counts[(pow(x, 3, p) + a * x + b) % p]
                   for x in range(p))  # includes the point at infinity


def read_int(label):
    return int(input(label))


def main():
    print('CRYPTOGRAPHY MATHS TOOLKIT')
    while True:
        print('\n1 Modular addition\n2 Modular subtraction\n3 Modular exponentiation')
        print('4 Modular inverse\n5 Prime check\n6 Elliptic-curve point count\n0 Exit')
        try:
            choice = input('Choose an option: ').strip()
            if choice == '0':
                break
            if choice in {'1', '2', '3'}:
                a = read_int('First integer / message: ')
                b = read_int('Second integer / exponent: ')
                n = read_int('Modulus: ')
                function = {'1': mod_add, '2': mod_subtract, '3': modular_power}[choice]
                print('Result:', function(a, b, n))
            elif choice == '4':
                a, n = read_int('Integer: '), read_int('Modulus: ')
                answer = mod_inverse(a, n)
                if answer is None:
                    print('No inverse exists: the integer and modulus are not coprime.')
                else:
                    print('Inverse:', answer)
                    print('Check (integer × inverse) mod modulus:', (a * answer) % n)
            elif choice == '5':
                n = read_int('Integer (absolute value at most 10000000): ')
                if abs(n) > 10000000:
                    raise ValueError('Use a smaller integer for this trial-division demo.')
                print('Prime:', is_prime(n))
            elif choice == '6':
                a, b, p = read_int('Coefficient a: '), read_int('Coefficient b: '), read_int('Prime p: ')
                print('Points, including infinity:', count_curve_points(a, b, p))
            else:
                print('Choose an option from 0 to 6.')
        except ValueError as error:
            print('Input error:', error)
        except (EOFError, KeyboardInterrupt):
            print('\nFinished.')
            break


if __name__ == '__main__':
    main()
