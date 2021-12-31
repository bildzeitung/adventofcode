#!/usr/bin/env python
"""
    Day 16
"""
import sys
from pathlib import Path


def packet(binrep, version):
    # read 3 bits for version
    v, binrep = int(binrep[:3], 2) + version, binrep[3:]
    # print(f"Version: {v}")
    # read 3 bits for type
    t, binrep = int(binrep[:3], 2), binrep[3:]
    # print(f"Type: {t}")
    if t == 4:
        total_bin = ""
        while True:
            flag, n, binrep = int(binrep[:1]), binrep[1:5], binrep[5:]
            total_bin += n
            if not flag:  # last packet
                # print(f"Integer: {int(total_bin, 2)}")
                return binrep, v

    # operator
    ltid, binrep = int(binrep[:1], 2), binrep[1:]
    if ltid == 0:
        # 15 bit total length
        l, binrep = int(binrep[:15], 2), binrep[15:]
        # print(f"Total length: {l}")
        to_run, binrep = binrep[:l], binrep[l:]
        while to_run:
            to_run, v = packet(to_run, v)
    else:
        # 11 bit number of subpackets
        l, binrep = int(binrep[:11], 2), binrep[11:]
        # print(f"Total subpackets: {l}")
        for _ in range(l):
            binrep, v = packet(binrep, v)

    return binrep, v  # what's left


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
