#!/usr/bin/env python
"""
  Day 19
"""
import re
import sys


def resolve(rules, rule):
  if '|' in rule:  # alternation
    left, right = [x.strip() for x in rule.split("|")]
    return f"({resolve(rules, left)}|{resolve(rules, right)})"
  if '"' in rule:  # base rule
    return rule.split('"')[1]

  # sequence of rules
  subrules = [x.strip() for x in rule.split(' ')]
  return "".join([resolve(rules, rules[x]) for x in subrules])


def main():
  rules = {}
  with open(sys.argv[1]) as f:
    # rules
    while line := f.readline().strip():
      num, rule = [x.strip() for x in line.split(":")]
      rules[num] = rule
    
    # messages
    messages = [line.strip() for line in f]

  # create a regex out of the rule sets
  r0 = f'^{resolve(rules, rules["0"])}$'
  print(f"Master rule: {r0}")
  rc = re.compile(r0)
  m = {x for x in messages if rc.search(x)}
  print(f"Found {m}")

  return len(m)


if __name__ == "__main__":
    print(main())