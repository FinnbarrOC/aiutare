FILENAME = "bin/benching/errors.txt"


def create_error_file():
    file = open(FILENAME, "w")
    file.write("Errors:0\n")
    file.flush()
    file.close()


def write_error(solver, instance, error):
    try:
        with open(FILENAME, "r") as f:
            arr_lines = f.readlines()
        with open(FILENAME, "w") as f:
            num_errors = int(arr_lines[0][arr_lines[0].rindex(":") + 1:])
            num_errors += 1
            f.write("Errors:" + str(num_errors) + "\n")
            for i in range(len(arr_lines) - 1):
                f.write(arr_lines[i + 1].strip("\n") + "\n")
            f.write(solver + " " + instance + "\n" + error)
    except Exception as exc:
        print("\nException caused while writing to error file:")
        print(exc)


def read_num_errors():
    try:
        with open(FILENAME, "r") as f:
            arr_lines = f.readlines()
            num_errors = arr_lines[0][arr_lines[0].rindex(":") + 1:].strip("\n")
            if int(num_errors) > 0:
                print("\nThere are " + num_errors + " errors. You can see them in " + FILENAME + ".")
            print('\n')
    except Exception as exc:
        print("\nException caused while reading from error file:")
        print(exc)
