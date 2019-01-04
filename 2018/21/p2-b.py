#!/usr/bin/env python


def main():
    vals = []
    r3 = 0
    r4 = r3 | 65536
    r3 = 10649702
    while True:
        r3 = (r3 + (r4 & 255)) & 16777215
        r3 = (r3 * 65899) & 16777215

        if r4 < 256:
            if r3 not in vals:
                vals.append(r3)
            else:
                print(vals)
                # puzzle answer is the last one in the sequence
                print("FINAL", vals[-1])
                return
            # printf("%ld\n", r3)
            r4 = r3 | 65536
            r3 = 10649702
        else:
            r4 = r4 >> 8


if __name__ == "__main__":
    main()
