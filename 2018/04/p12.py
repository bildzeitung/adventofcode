#!/usr/bin/env python
""" Day 4

    Read the data and create a ledger where each guard and minute are
    indexed. From there, the various strategies can be summarized.

    n.b. the data file from the site must be sorted before this program
         can use it

    This is an all-in-one for both parts.
"""
import re
import sys
from pathlib import Path

GUARD_RE = re.compile(r"#(\d+)")
MINUTE_RE = re.compile(r":(\d\d)")


def main():
    summary = {}
    with Path(sys.argv[1]).open() as f:
        guard = None
        start_nap = None
        end_nap = None
        for line in f:
            """ Simple state machine

                - if there's a guard line, save the guard
                - if it's a start line, then set the start line
                - if it's a wake up line, then save the range
            """
            if "Guard" in line:
                guard = int(GUARD_RE.search(line).groups()[0])
                continue

            minute = int(MINUTE_RE.search(line).groups()[0])
            if "falls asleep" in line:
                start_nap = minute
                continue

            # it's a wake up line
            assert "wakes up" in line
            end_nap = minute

            # process the guard into the summary
            if guard not in summary:
                summary[guard] = {"minutes": [0] * 60}

            for i in range(start_nap, end_nap):
                summary[guard]["minutes"][i] += 1

            summary[guard]["total"] = sum(summary[guard]["minutes"])
            summary[guard]["max"] = max(summary[guard]["minutes"])

    print(summary)

    """ Part 1 solution
    """
    sleepiest = max(summary, key=lambda x: summary[x]["total"])
    sleepiest_minute = summary[sleepiest]["minutes"].index(
        max(summary[sleepiest]["minutes"])
    )
    print("SLEEPIEST GUARD, MINUTE", sleepiest, sleepiest_minute)
    print("PART 1 CODE", sleepiest * sleepiest_minute)

    """ Part 2 solution
    """
    most_overlap = max(summary, key=lambda k: summary[k]["max"])
    most_overlap_minute = summary[most_overlap]["minutes"].index(
        max(summary[most_overlap]["minutes"])
    )
    print("MOST CONSISTENT GUARD, MINUTE", most_overlap, most_overlap_minute)
    print("PART 2 CODE", most_overlap * most_overlap_minute)


if __name__ == "__main__":
    main()
