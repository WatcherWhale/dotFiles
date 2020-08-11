#!/bin/sh

server="$(nordvpn status | grep -w "server" | awk -F ': ' '{ print $2 }' | awk -F '.' '{ print $1 }')"


if [ "$server" == "" ]; then
    echo "%{F#bf616a}  %{F#88c0d0}Disconnected"
else
    echo "%{F#a3be8c}  %{F#88c0d0}$server"
fi
