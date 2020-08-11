#!/bin/sh

killall mpv
killall xwinwrap

for m in $(xrandr --query | grep -w connected | grep -v primary | cut -d" " -f1)
do
    geom="$(xrandr | grep -w $m | cut -d" " -f3)"
    xwinwrap -ov -ni -g $geom -- mpv -vo x11 -wid WID --keepaspect=yes --loop $1 &
done

for m in $(xrandr --query | grep -w connected | grep primary | cut -d" " -f1)
do
    geom="$(xrandr | grep -w $m | cut -d" " -f4)"
    xwinwrap -ov -ni -g $geom -- mpv -vo x11 -wid WID --keepaspect=yes --loop $1 &
done
