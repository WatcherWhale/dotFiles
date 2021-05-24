#!/usr/bin/env bash

if [ "$1" = "dim" ]; then
    brillo -S 1
elif [ "$1" = "bright" ]; then
    brillo -S 100
else
    negative=$(( $1 < 0 ))

    if [ $negative -eq 1 ]; then
        let bright=-1*$1
        brillo -U $bright
    else
        brillo -A $1
    fi
fi

brillo > /tmp/brillo
