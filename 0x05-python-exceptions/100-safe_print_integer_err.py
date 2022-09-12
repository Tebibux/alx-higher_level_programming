#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as alx:
        sys.stderr.write("Exception: {}\n".format(alx))
        return (False)
    else:
        return (True)
