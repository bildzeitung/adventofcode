#!/bin/bash

# change \[\|"] to +
# change \x to ---
# remove all letters & numbers
#
# This leaves us with the delta between coding and actual
# so just get the length and then sum them all up
perl -ne 'chomp; s/\\[^x]/+/g; s/\\x/---/g; s/\w//g ; print length($_), "\n"' < matchsticks.in | paste -sd+ - | bc
