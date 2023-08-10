#!/usr/bin/python3

ch = 0
for j in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(j - ch)), end="")
    ch = 32 if ch == 0 else 0
