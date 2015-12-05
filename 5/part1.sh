#!/bin/bash

# - double letters ---------- at least 3 vowels -------- and not ab, cd, pq, or xy ---
egrep '(.)\1' $1 | egrep '[aeiou].*[aeiou].*[aeiou]' | egrep -v '(ab)|(cd)|(pq)|(xy)' | wc -l
