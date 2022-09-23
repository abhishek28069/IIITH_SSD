#!/bin/bash

ls -lh . | grep -E -o "[-drwx]{10}" | grep -E "[-d][-rwx]{2}x[-rwx]{3}-[-rwx]{2}"

for file in *; do
    if [ -f $file ]; then
        if [ $(ls -lh $file | grep -E -o "[-drwx]{10}" | grep -E "[-d][-rwx]{2}x[-rwx]{3}-[-rwx]{2}" | wc -l) -ne 0 ]; then
            echo $file
        fi
    fi

done
