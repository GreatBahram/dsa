from typing import List


def poly_hash(string: str, prime: int, multiplier: int) -> int:
    ans = 0
    for c in reversed(string):
        ans = (ans * multiplier + ord(c)) % prime
    return ans


def naive_get_occurrences(text, pattern) -> List[int]:
    n = len(text)
    k = len(pattern)
    return [i for i in range(n - k + 1) if text[i : i + k] == pattern]


def precompute_hashes(
    text: str, pattern_length: int, prime: int = 1_000_000_007, multiplier: int = 263
) -> List[int]:
    """Compute hashes for all patterns inside the a given string."""
    n = len(text)
    k = pattern_length

    T = [ord(char) for char in text]
    hashes = [None] * (n - k + 1)

    # calcualte the hash for the last substring
    hashes[-1] = poly_hash(text[n - k :], prime, multiplier)

    y = 1
    for i in range(k):
        y = (y * multiplier) % prime

    for i in range(n - k - 1, -1, -1):
        hashes[i] = (multiplier * hashes[i + 1] + T[i] - y * T[i + k]) % prime
    return hashes


def rabin_karp(text: str, pattern: str) -> List[int]:
    prime = 1_000_000_007
    multiplier = 263
    results = []

    ptrn_hash = poly_hash(pattern, prime, multiplier)

    n = len(text)
    k = len(pattern)

    hashes = precompute_hashes(text, k, prime, multiplier)

    for i in range(n - k + 1):
        if ptrn_hash != hashes[i]:
            continue
        if pattern == text[i : i + k]:
            results.append(i)
    return results


if __name__ == "__main__":
    pattern = input().rstrip()
    text = input().rstrip()

    resutls = rabin_karp(text, pattern)

    print(" ".join(map(str, resutls)))
