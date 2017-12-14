#!/bin/bash

# ----------- remove all letters ------ add 2 for beginning and ending quotes
perl -ne 'chomp; s/\w//g; print length($_)+2, "\n"' < matchsticks.in | paste -sd+ - | bc
