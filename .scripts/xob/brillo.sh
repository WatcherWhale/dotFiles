#!/bin/sh

negative=$(( $1 < 0 ))

if [ $negative -eq 1 ]; then
    let bright=-1*$1
    brillo -U $bright
else
    brillo -A $1
fi

brillo > /tmp/brillo
