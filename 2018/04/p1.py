#!/usr/bin/env python
''' Day 4

    Read the data and create a ledger where each guard and minute are
    indexed. From there, the various strategies can be summarized.

    n.b. the data file from the site must be sorted before this program
         can use it
'''
import re
import sys
from collections import defaultdict
from pathlib import Path

GUARD_RE = re.compile(r'#(\d+)')
MINUTE_RE = re.compile(r':(\d\d)')


def main():
    ledger = defaultdict(list)
    with Path(sys.argv[1]).open() as f:
        guard = None
        start_nap = None
        end_nap = None
        for line in f:
            ''' Simple state machine

                - if there's a guard line, save the guard
                - if it's a start line, then set the start line
                - if it's a wake up line, then save the range
            '''
            if 'Guard' in line:
                guard = GUARD_RE.search(line).groups()[0]
                continue

            minute = int(MINUTE_RE.search(line).groups()[0])
            if 'falls asleep' in line:
                start_nap = minute
                continue

            # it's a wake up line
            assert('wakes up' in line)

            end_nap = minute
            ledger[guard].append((start_nap, end_nap))

            # a guard against incomplete / open ranges, but fortunately
            # the data set is clean for this case
            start_nap = None
            end_nap = None

    print(ledger)
    summary = {}
    ''' Summarize the data

        In theory, this could be done while the data is being read in,
        but keeping it as a separate step seems more readable
    '''
    for guard in ledger:
        minutes = [0] * 60
        for item in ledger[guard]:
            start, finish = item
            for i in range(start, finish):
                minutes[i] += 1
            summary[int(guard)] = {'minutes': minutes,
                                   'total': sum(minutes)}

    print(summary)

    ''' Now sort out the answer to the problem
    '''
    # sort the summary by total sleep time; pick the largest
    sleepiest = max(summary, key=lambda x: summary[x]['total'])
    print('SLEEPIEST GUARD', sleepiest,
          'TOTAL ASLEEP:', summary[sleepiest]['total'])

    # grab the index of where the largest value is
    sleepiest_minute = summary[sleepiest]['minutes'].index(
            max(summary[sleepiest]['minutes'])
            )
    print('SLEEPIEST MINUTE', sleepiest_minute)

    print('CODE', sleepiest * sleepiest_minute)


if __name__ == "__main__":
    main()
