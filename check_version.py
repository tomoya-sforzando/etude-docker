#!/usr/bin/env python3
import sys
print(sys.version)

old, new = 0, 1
for i in range(10):
    print(f"{i=}, {old=}, {new=}")
    old = new
    new = old + new
