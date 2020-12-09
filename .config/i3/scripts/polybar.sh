#!/usr/bin/env sh

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -x polybar >/dev/null; do sleep 1; done

# Launch polybar
# polybar top &


for m in $(xrandr --query | grep " connected" | grep -v " primary" | cut -d" " -f1); 
do
    echo $m
    MONITOR=$m polybar -c $HOME/.config/polybar/dark-config nord-top &
done


for m in $(xrandr --query | grep " connected" | grep " primary" | cut -d" " -f1); 
do
    echo $m
    MONITOR=$m polybar -c $HOME/.config/polybar/dark-config nord-top &
    MONITOR=$m polybar -c $HOME/.config/polybar/dark-config nord-down &
done
