#!/usr/bin/python3
for Mynum in range(ord('a'), ord('z') + 1):
    if chr(Mynum) != 'e' and chr(Mynum) != 'q':
        print("{:c}".format(Mynum), end='')
