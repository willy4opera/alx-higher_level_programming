#!/usr/bin/python3ads from standard input and computes metrics.

"""
At the keyboard interruption,after every ten lines or a (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """Here, we Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    d_size = 0
    d_status_codes = {}
    d_valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    d_count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(d_size, d_status_codes)
                d_count = 1
            else:
                d_count += 1

            line = line.split()

            try:
                d_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if d_status_codes.get(line[-2], -1) == -1:
                        d_status_codes[line[-2]] = 1
                    else:
                        d_status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(d_size, d_status_codes)

    except KeyboardInterrupt:
        print_stats(d_size, d_status_codes)
        raise
