#!/bin/sh

killall xob

# Create FIFO's and start listeners
rm -f /tmp/brillo
mkfifo /tmp/brillo
tail -f /tmp/brillo | xob -s brillo &

~/.scripts/xob/audio.py | xob -s audio &
