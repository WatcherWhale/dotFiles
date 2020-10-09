#!/bin/sh
# speed.sh: a very tiny utility to measure typing speed.
prompt="Start typing a piece of text. Press Ctrl-d twice to finish."
echo "\n$prompt \n"
start_time=`date +%s`
words=`cat|wc -w`
end_time=`date +%s`
speed=`echo "scale=2; $words / ( ( $end_time - $start_time ) / 60)" | bc`
echo "\n\nYou have a typing speed of $speed words per minute."
