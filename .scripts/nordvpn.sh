#!/bin/sh

server="$(nordvpn status | grep -w "server" | awk -F ': ' '{ print $2 }' | awk -F '.' '{ print $1 }' | cut -c1-2 | tr [a-z] [A-Z])"


if [ "$server" == "" ]; then
    echo "%{F#bf616a}"
else
    echo "%{F#a3be8c}"
fi
