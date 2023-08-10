#!/usr/bin/python3
for charc in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format((charc - (ord('a') - ord('A'))) if charc % 2 else charc), end='')
