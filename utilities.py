import itertools
import math
from typing import List, Dict


def fibonacci_sequence():
    second_previous_value = 1
    previous_value = 2
    yield second_previous_value
    yield previous_value
    while True:
        next_value = second_previous_value + previous_value
        second_previous_value = previous_value
        previous_value = next_value
        yield next_value


def triangle_numbers():
    previous_iteration = 0
    cumulative_sum = 0
    while True:
        next_iteration = previous_iteration + 1
        cumulative_sum += next_iteration
        previous_iteration = next_iteration
        yield cumulative_sum


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(2, num):
        if i*i > num:
            break
        if num % i == 0:
            return False

    return True


def is_palindrome(value: int or str):
    str_version = str(value)
    num_digits_to_check = len(str_version) // 2
    for i in range(0, num_digits_to_check + 1):
        if str_version[i] != str_version[(i + 1) * -1]:
            return False

    return True


def all_prime_numbers():
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 1


def all_primes_up_to(n: int) -> List[int]:
    # Sieve of Eratosthenes
    # Roughly O(n) implementation
    candidates = [i for i in range(n + 1)]
    primes_mask = [True] * len(candidates)
    square_root = round(math.sqrt(n))
    if n < 2:
        return []

    for i in range(square_root):
        if i < 2:
            primes_mask[i] = False
        if not primes_mask[i]:
            continue
        for j in range(i + candidates[i], len(candidates), candidates[i]):
            if not primes_mask[j]:
                continue

            primes_mask[j] = False

    primes = [candidates[i] for i in range(len(candidates)) if primes_mask[i]]
    return primes


def all_triangle_numbers():
    i = 1
    while True:
        yield nth_triangle_number(i)
        i += 1


def calculate_divisors(num):
    divisors = [1, num]
    square_root = int(math.sqrt(num))

    if square_root * square_root == num:
        # Num is perfect square
        divisors.append(square_root)

    for i in range(2, square_root + 1):
        if num % i == 0:
            divisors.append(i)
            divisors.append(num // i)

    return list(set(divisors))


def collatz_step(num):
    if num % 2 == 0:
        return num // 2
    return (num * 3) + 1


def integer_to_words(number):
    def digit_to_word(digit):
        if digit == 0:
            return ""
        if digit == 1:
            return "one"
        if digit == 2:
            return "two"
        if digit == 3:
            return "three"
        if digit == 4:
            return "four"
        if digit == 5:
            return "five"
        if digit == 6:
            return "six"
        if digit == 7:
            return "seven"
        if digit == 8:
            return "eight"
        if digit == 9:
            return "nine"

    if number == 1000:
        return "one thousand"
    if number >= 100:
        partial_answer = digit_to_word(number // 100) + ' hundred '
        if number % 100 != 0:
            partial_answer += 'and '
            return partial_answer + integer_to_words(number % 100)

    if number >= 20:
        if number <= 29:
            partial_answer = "twenty"
        elif number <= 39:
            partial_answer = "thirty"
        elif number <= 49:
            partial_answer = "forty"
        elif number <= 59:
            partial_answer = "fifty"
        elif number <= 69:
            partial_answer = "sixty"
        elif number <= 79:
            partial_answer = "seventy"
        elif number <= 89:
            partial_answer = "eighty"
        elif number <= 99:
            partial_answer = "ninety"

        if number % 10 != 0:
            partial_answer += '-' + digit_to_word(number % 10)

        return partial_answer

    if number < 10:
        return digit_to_word(number)

    if number == 10:
        return "ten"
    if number == 11:
        return "eleven"
    if number == 12:
        return "twelve"
    if number == 13:
        return "thirteen"
    if number == 14:
        return "fourteen"
    if number == 15:
        return "fifteen"
    if number == 16:
        return "sixteen"
    if number == 17:
        return "seventeen"
    if number == 18:
        return "eighteen"
    if number == 19:
        return "nineteen"


def get_proper_divisors(number):
    divisors = calculate_divisors(number)
    divisors.remove(number)
    return divisors


def prime_factorization(number):
    # ~ O(sqrt(n))
    if number == 1:
        return [1]
    if number == 3:
        return [3]
    factors = []
    prime_generator = all_prime_numbers()
    primes = []
    while len(primes) == 0 or primes[-1] <= int(math.sqrt(number)) + 1:
        primes.append(next(prime_generator))

    for prime in primes:
        number_copy = number
        while number_copy % prime == 0:
            factors.append(prime)
            number_copy = number_copy / prime
            if not number_copy.is_integer():
                break

    product = 1
    for factor in factors:
        product *= factor

    if product != number:
        dividend = number / product
        if dividend.is_integer() and is_prime(int(dividend)):
            factors.append(int(dividend))

    final_product = 1
    for factor in factors:
        final_product *= factor

    assert final_product == number

    return factors


def prime_factorization_with_powers(num: int) -> Dict[int, int]:
    factorization = prime_factorization(num)
    factorization_with_powers = dict()
    for i in range(len(factorization)):
        for j in range(i + 1, len(factorization) + 1):
            if factorization[i] in factorization_with_powers.keys():
                break
            try:
                if factorization[j] != factorization[i]:
                    factorization_with_powers[factorization[i]] = j - i
            except IndexError:
                factorization_with_powers[factorization[i]] = j - i

    return factorization_with_powers


def solve_quadratic(a, b, n):
    return math.pow(n, 2) + (a * n) + b


def to_binary_string(num: int) -> str:
    reverse_binary_string = ''
    if num == 0:
        return '0'
    while num > 0:
        reverse_binary_string += str(num % 2)
        num = num // 2
    return reverse_binary_string[::-1]


def generate_rotations(num: int) -> List[int]:
    rotations = []
    string_num = str(num)
    for i in range(len(string_num)):
        rotations.append(int(string_num[i:] + string_num[:i]))
    return rotations


def nth_triangle_number(n: int) -> int:
    return int(n * (n + 1) / 2)


def nth_square_number(n: int) -> int:
    return n * n


def nth_pentagonal_number(n: int) -> int:
    return int(n * (3 * n - 1) / 2)


def nth_hexagonal_number(n: int) -> int:
    return int(n * (2 * n - 1))


def nth_heptagonal_number(n: int) -> int:
    return int(n * (5 * n - 3) / 2)


def nth_octagonal_number(n: int) -> int:
    return int(n * (3 * n - 2))


def is_triangle_number(num: int) -> bool:
    doubled_num = num * 2
    truncated_square_root = int(math.sqrt(doubled_num))
    if doubled_num / truncated_square_root == (truncated_square_root + 1):
        return True
    return False


def is_square(num: int) -> bool:
    return math.sqrt(num).is_integer()


def is_pentagonal(num: int) -> bool:
    # O(1)
    # Inverse pentagonal number function
    pentagonal_index = (1 + math.sqrt(1 + 24 * num)) / 6
    return pentagonal_index.is_integer()


def is_hexagonal(num: int) -> bool:
    # O(1)
    # Inverse hexagonal formula
    hexagonal_index = (1 + math.sqrt(1 + 8 * num)) / 4
    return hexagonal_index.is_integer()


def is_permutation(candidate: int or str, original: int or str) -> bool:
    sorted_str_candidate = sorted(str(candidate))
    sorted_str_original = sorted(str(original))
    return sorted_str_candidate == sorted_str_original


def all_string_permutations(value: int or str):
    permutations = set(map(''.join, itertools.permutations(str(value))))
    return permutations


def is_one_through_n_pandigital(num: int) -> bool:
    num_string = str(num)
    if len(num_string) > 9:
        return False

    permuted_pandigital = ''.join([str(i + 1) for i in range(len(num_string))])
    return is_permutation(num_string, permuted_pandigital)


def get_letter_score(letter):
    return ord(letter) - 64


def get_word_score(word):
    cumulative_score = 0
    for letter in word:
        cumulative_score += get_letter_score(letter)
    return cumulative_score


def n_choose_r(n: int, r: int) -> int:
    return int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))


def digit_sum(num: int) -> int:
    str_num = str(num)
    return sum([int(char) for char in str_num])


def reduce_fraction_to_simplest_terms(frac: (int, int)) -> (int, int):
    numer_factors = prime_factorization_with_powers(frac[0])
    denom_factors = prime_factorization_with_powers(frac[1])
    reduced_numerator = frac[0]
    reduced_denominator = frac[1]
    for factor, power in numer_factors.items():
        if factor in denom_factors:
            cancelled_power = min(power, denom_factors[factor])
            cancelled_factor = pow(factor, cancelled_power)
            reduced_numerator /= cancelled_factor
            reduced_denominator /= cancelled_factor

    return int(reduced_numerator), int(reduced_denominator)


def add_fractions(a: (int, int), b: (int, int)) -> (int, int):
    if a[1] != b[1]:
        common_denominator = a[1] * b[1]
        a = (a[0] * (common_denominator // a[1]), common_denominator)
        b = (b[0] * (common_denominator // b[1]), common_denominator)
    else:
        common_denominator = a[1]

    return a[0] + b[0], common_denominator


def multiply_fractions(a: (int, int), b: (int, int)) -> (int, int):
    return reduce_fraction_to_simplest_terms((a[0] * b[0], a[1] * b[1]))


def divide_fractions(a: (int, int), b: (int, int)) -> (int, int):
    return multiply_fractions((fraction_inverse(a)), b)


def fraction_inverse(frac: (int, int)) -> (int, int):
    return frac[1], frac[0]


def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        t = b
        b = a % b
        a = t

    return a
