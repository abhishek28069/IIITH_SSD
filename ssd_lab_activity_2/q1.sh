#!/bin/bash
# echo "file content"
#cat $1
total=0
middle=0
total=$(wc -l $1 | awk -F " " '{print $1}')
# echo $total
((middle = (total + 1) / 2))
# echo $middle
awk "NR==$middle" $1
