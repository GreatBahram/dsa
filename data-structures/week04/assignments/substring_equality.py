import sys


def are_equal(hashes1, hashes2, prime1, prime2, x, a, b, l) -> bool:
    y1 = pow(x, l, prime1)
    y2 = pow(x, l, prime2)

    a_hash1 = hash_value(hashes1, y1, a, l) % prime1
    a_hash2 = hash_value(hashes2, y2, a, l) % prime2
    b_hash1 = hash_value(hashes1, y1, b, l) % prime1
    b_hash2 = hash_value(hashes2, y2, b, l) % prime2

    return a_hash1 == b_hash1 and a_hash2 == b_hash2


def hash_value(hashes, y, start_idx, length: int) -> int:
    return hashes[start_idx + length] - y * hashes[start_idx]


if __name__ == "__main__":
    text = sys.stdin.readline()
    n_queries = int(sys.stdin.readline())

    # To further reduce the probability of a collision,
    # one may take two different modulus
    prime1 = 10 ** 9 + 7
    prime2 = 10 ** 9 + 9
    x = 263
    h1 = [0] * (len(text) + 1)
    h2 = [0] * (len(text) + 1)

    # compute hashes for all prefixes
    for i in range(1, len(text) + 1):
        h1[i] = (h1[i - 1] * x + ord(text[i - 1])) % prime1
        h2[i] = (h2[i - 1] * x + ord(text[i - 1])) % prime2

    for i in range(n_queries):
        a, b, l = map(int, sys.stdin.readline().split())
        print("Yes" if are_equal(h1, h2, prime1, prime2, x, a, b, l) else "No")
