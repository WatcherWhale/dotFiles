#!/usr/bin/env bash

playerctl play-pause

if [ "$(playerctl)" == "Playing" ]; then
    polybar-msg hook playerctl 1
else
    polybar-msg hook playerctl 2
fi
