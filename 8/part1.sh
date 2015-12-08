#!/bin/bash

# change \\ to .
# change \x00 to ---
# change \" to + 
# remove all letters
#
# This leaves us with the delta between coding and actual
# so just get the length and then sum them all up
perl -ne 'chomp ; s/\\\\/./g ; s/\\x[0-9a-f][0-9a-f]/---/g ; s/\\"/+/g ; s/[a-z]//g ; print length($_), "\n"' < matchsticks.in | paste -sd+ - | bc
