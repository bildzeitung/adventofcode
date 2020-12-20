#!/usr/bin/env python
"""
  Day 19
"""
import re
import sys


def resolve(rules, rule):
    if '"' in rule:  # base rule
        return rule.split('"')[1]
    if "|" in rule:  # alternation
        left, right = [x.strip() for x in rule.split("|")]
        return f"({resolve(rules, left)}|{resolve(rules, right)})"

    # sequence of rules
    subrules = [x.strip() for x in rule.split(" ")]
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

    # Rule replacements:
    #   8: 42 | 42 8
    # I think this is {42}+ (ie. one or more instances of Rule 42)
    rule42 = resolve(rules, "42")
    print(f"Rule 42: {rule42}")
    print(f"Rule 42: {resolve(rules, '31')}")
    rules["42"] = f'"({rule42})+"'
    #
    # Just expand manually and hoping it's finite
    #
    rules["11"] = "42 31 | 990"
    rules["990"] = "42 42 31 31 | 991"
    rules["991"] = "42 42 42 31 31 31 | 992"
    rules["992"] = "42 42 42 42 31 31 31 31 | 993"
    rules["993"] = "42 42 42 42 42 31 31 31 31 31"

    # create a regex out of the rule sets
    r0 = f'^{resolve(rules, rules["0"])}$'
    rc = re.compile(r0)
    m = {x for x in messages if rc.search(x)}
    print(f"Found {m}")

    return len(m)


if __name__ == "__main__":
    print(main())
