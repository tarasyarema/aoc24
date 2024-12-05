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


def main():
    a1 = 1
    a2 = 1

    ...

    print(f"#1: {a1}")

    ...

    print(f"#2: {a2}")


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

