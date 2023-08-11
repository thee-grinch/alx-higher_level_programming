#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j and (i+j != 17):
            print("{}{}, ".format(i, j), end="")
else:
    print(f"{89}")
