import os
import sys


TPL_FILE = "__tpl__.py"


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception("Invalid number of arguments")

    try:
        f = int(sys.argv[1])

    except ValueError:
        raise Exception(f"Invalid argument type: {sys.argv[1]}")

    dir_name = f"{f}"
    main_file = f"{dir_name}/main.py"

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    if os.path.exists(main_file):
        print(f"> File already exists: {main_file}")

    else:
        with open(f"{dir_name}/main.py", 'w') as fb:
            with open(TPL_FILE, 'r') as tpl:
                fb.write(tpl.read())

        print(f"Created file: {main_file}")

    test_files = [
        f"{dir_name}/test.txt",
        f"{dir_name}/in.txt",
    ]

    for test_file in test_files:
        if os.path.exists(test_file):
            print(f"> File already exists: {test_file}")

        else:
            with open(test_file, 'w') as fb:
                fb.write("")

            print(f"Created test file: {test_file}")

    print(f"Setup complete for challenge: {f}")
    sys.exit(0)
