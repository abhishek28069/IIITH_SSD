#!/bin/bash
#usage bash q1.sh input1.txt

cat $1 | grep -E -wio "a\w*.\w*" | grep -E -iv "txt\b"
