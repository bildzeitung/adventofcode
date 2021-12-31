#!/usr/bin/env python
"""
    Day 16
"""
import sys
from pathlib import Path
import math


def packet(binrep, value):
    # read 3 bits for version
    v, binrep = int(binrep[:3], 2), binrep[3:]
    # read 3 bits for type
    t, binrep = int(binrep[:3], 2), binrep[3:]
    print(f"Type: {t}")
    if t == 4:
        total_bin = ""
        while True:
            flag, n, binrep = int(binrep[:1]), binrep[1:5], binrep[5:]
            total_bin += n
            if not flag:  # last packet
                # print(f"Integer: {int(total_bin, 2)}")
                return binrep, int(total_bin, 2)

    # operator
    values = []
    ltid, binrep = int(binrep[:1], 2), binrep[1:]
    if ltid == 0:
        # 15 bit total length
        l, binrep = int(binrep[:15], 2), binrep[15:]
        # print(f"Total length: {l}")
        to_run, binrep = binrep[:l], binrep[l:]
        while to_run:
            to_run, v = packet(to_run, value)
            values.append(v)
    else:
        # 11 bit number of subpackets
        l, binrep = int(binrep[:11], 2), binrep[11:]
        # print(f"Total subpackets: {l}")
        for _ in range(l):
            binrep, v = packet(binrep, value)
            values.append(v)

    if t == 0:
        return binrep, sum(values)
    if t == 1:
        return binrep, math.prod(values)
    if t == 2:
        return binrep, min(values)
    if t == 3:
        return binrep, max(values)
    if t == 5:
        return (binrep, 1) if values[0] > values[1] else (binrep, 0)
    if t == 6:
        return (binrep, 1) if values[0] < values[1] else (binrep, 0)
    if t == 7:
        return (binrep, 1) if values[0] == values[1] else (binrep, 0)
    return binrep, "wtf"  # what's left


def make_binrep(line: str) -> str:
    return "".join(bin(int(c, 16))[2:].zfill(4) for c in line)


def main():
    with Path(sys.argv[1]).open() as f:
        for line in f:
            print(f"Processing: {line.strip()}")
            _, version = packet(make_binrep(line.strip()), 0)
            print(f"-{version}-")


if __name__ == "__main__":
    main()
