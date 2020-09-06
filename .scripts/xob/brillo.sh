#!/bin/sh

if [ "$1" = "dim" ]; then
    xbacklight -set 1
elif [ "$1" = "bright" ]; then
    xbacklight -set 100
else
    negative=$(( $1 < 0 ))

    if [ $negative -eq 1 ]; then
        let bright=-1*$1
        xbacklight -dec $bright
    else
        xbacklight -inc $1
    fi
fi

xbacklight -get > /tmp/brillo
