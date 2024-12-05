import sys
import time


def with_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} executed in {end - start} seconds")
        return result

    return wrapper


def main(data: list[list[int]]):
    a1 = []
    oks = []

    for d in data:
        ok = 0

        op = lambda x, y: y - x

        if d[0] > d[-1]:
            op = lambda x, y: x - y

        curr_ok = []
        done = False

        for i, k in enumerate(d):
            if i == 0:
                continue

            t = op(d[i-1], k)
            curr_ok.append(t)

            if t <= 0 or t > 3:
                ok = t
                done = True

        oks.append((not done, curr_ok))

        if not done:
            a1.append(
                1 if ok == 0 else 0
            )

    print(f"#1: {sum(a1)}")

    ok_c = 0

    for i, (ok, o) in enumerate(oks):

        if ok:
            ok_c += 1
            continue

        s = sum(1 if x <= 0 and x >= -3 else 0 for x in o)
        s2 = sum(1 if x > 3 else 0 for x in o)

        if s == 1 and s2 == 0:
            print(f"> {i}: {data[i]} / {o} / {s}")
            ok_c += 1
            continue

        if s > 1:
            continue

        if s2 == 1:
            if abs(o[0]) > 3 or abs(o[-1]) > 3:
                print(f">> {i}: {data[i]} / {o} / {s} / {s2}")
                ok_c += 1
                continue


    print(f"#2: {ok_c}")


if __name__ == '__main__':
    f = "test.txt"

    # check args
    if len(sys.argv) > 1:
        f = sys.argv[1]

    with open(f, 'r') as fb:
        with_timer(main)([
            [
                int(s.strip()) for s in line.split(" ")
            ]
            for line in fb.readlines()
        ])

