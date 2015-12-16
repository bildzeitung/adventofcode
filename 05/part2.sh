#!/bin/bash

# -- two-char dupe -- <char1><char2><char1> -
egrep '(..).*\1' $1 | egrep '(.).\1' | wc -l
