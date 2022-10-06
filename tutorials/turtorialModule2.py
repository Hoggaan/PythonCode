def is_prime(n):
    """
    Return True if `n` is a prime; False otherwise.
    """
    if n < 2: 
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True
def prime_factors(n):
 """Returns the generator that makes an iterator for
 the prime factoris of `n`."""
 p = 2
 n = abs(n)
 for p in range(2, n):
    if n % p == 0 and is_prime(p):
        yield p
if __name__ == '__main__':
    n = int(input("n = "))
    print("Prime factors of {}: {}".format(n, ", ".join(str(x) for x in prime_factors(n))))
