"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    # Raise an error if the input is invalid
    if number_of_primes <= 0:
        raise ValueError
    list = []

    source_num = 2
    while number_of_primes > 0:
        is_prime = True
        for divisor in range(2, source_num):
            if source_num % divisor == 0:
                is_prime = False
                break

        if is_prime:
            list.append(source_num)
            number_of_primes -= 1

        source_num += 1

    return list
