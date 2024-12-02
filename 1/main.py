import sys
from collections import defaultdict


def main(d: list[list[int]]):
    l = sorted(d, key=lambda x: x[0])
    r = sorted(d, key=lambda x: x[1])

    print(f"#1: {sum(abs(i[0] - j[1]) for i, j in zip(l, r))}")

    sim = defaultdict(lambda: 0)

    for re in r:
        sim[re[1]] += 1

    print(f"#2: {sum(i[0] * sim[i[0]] for i in l)}")


if __name__ == '__main__':
    f = "test.txt"

    # check args
    if len(sys.argv) > 1:
        f = sys.argv[1]

    with open(f, 'r') as fb:
        main([
            [
                int(s.strip()) for s in line.split("   ")
            ]
            for line in fb.readlines()
        ])
