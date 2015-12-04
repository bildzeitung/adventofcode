#!/bin/bash
cat paren.in | perl -ne 'print join("\n",split //);' | sort | uniq -c

