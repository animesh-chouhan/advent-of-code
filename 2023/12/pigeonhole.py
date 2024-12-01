import itertools


def pigeonhole(n, m):
    """
    Generate the ways n balls can placed in m slots
    """
    for choice in itertools.combinations(range(n + m - 1), n):
        slot = [c - i for i, c in enumerate(choice)]
        result = [0] * m
        for i in slot:
            result[i] += 1
        yield result


if __name__ == "__main__":
    print(list(pigeonhole(5, 3)))
