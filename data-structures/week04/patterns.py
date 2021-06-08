def is_equal(str1: str, str2: str) -> bool:
    """
    Return True if str1 and str2 are the same string; False otherwise.

    Running time: O(|pattern|)
    """
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True


def find_pattern_naive(text, pattern):
    """
    Running time: O(|text| * |pattern|)

    >>> find_pattern_naive("bahram", "a")
    [1, 4]
    """
    result = []
    for i in range(len(text) - len(pattern) + 1):
        if is_equal(text[i : i + len(pattern)], pattern):
            result.append(i)
    return result


# lets improve the is_equal function a little bit using hash-function
# the idea is that we should only compare strings that their hashes are
# the same.
# if the Pattern != string, the probability Pr[h(P) == h(t)] is at most |P|/prime_number
# so if we choose a big prime number the probability will be very low.
def poly_hash(string: str, prime: int, multiplier: int) -> int:
    """
    Running time: O(|string|)
    """
    ans = 0
    for c in reversed(string):
        ans = (ans * multiplier + ord(c)) % prime
    return ans


def rabin_karp(text: str, pattern: str) -> List[int]:
    """
    The only difference between this implementation and find_pattern_naive
    is that we used a poly_hash for comparing two strings, but at the end
    the running time of both implementation is the same.
    """
    prime = 1_000_000_007
    multiplier = 263
    results = []

    ptrn_hash = poly_hash(pattern, prime, multiplier)

    for i in range(len(text) - len(pattern) + 1):
        t_hash = poly_hash(text[i : i + len(pattern)], prime, multiplier)

        if ptrn_hash != t_hash:
            continue

        # to handle false alarms
        if is_equal(text[i : i + len(pattern)], pattern):
            results.append(i)

    return results
