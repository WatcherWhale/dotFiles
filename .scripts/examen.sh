#!/usr/bin/env bash

xrandr --output eDP-1 --off
xrandr --output DP-1 --off

stylus=$(xsetwacom --list devices | grep "type: STYLUS" | awk -F'id:' '{print $1}' | awk '{$1=$1};1' | awk -F'\n' '{ print "\""$1"\"" }')
pad=$(xsetwacom --list devices | grep "type: PAD" | awk -F'id:' '{print $1}' | awk '{$1=$1};1' | awk -F'\n' '{ print "\""$1"\"" }')
monitor=$(autorandr | grep -w "(current)\|(detected)" | cut -d' ' -f1)

# Set button shortcuts
xsetwacom set "Wacom Intuos S Pad pad" Button 8 "key Delete"
xsetwacom set "Wacom Intuos S Pad pad" Button 1 "key ctrl" "key z"
xsetwacom set "Wacom Intuos S Pad pad" Button 2 "key ctrl" "key s"
xsetwacom set "Wacom Intuos S Pad pad" Button 3 "key Print"

i3 restart

killall kdeconnect-indi
killall kdeconnectd

sleep 3
xsetwacom set "Wacom Intuos S Pen stylus" MapToOutput 2560x1440+0+0
