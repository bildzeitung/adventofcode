#!/usr/bin/env python
from pathlib import Path


def main():
    with Path('./input.txt').open() as f:
        print(f"TOTAL: {sum(int(x.strip()) for x in f)}")


if __name__ == '__main__':
    main()
