#!/usr/bin/python3

for ch in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format((ch - (ord('a') - ord('A'))) if ch % 2 else ch), end='')
