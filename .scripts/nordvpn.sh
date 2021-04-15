#!/bin/sh

server="$(nordvpn status | grep -w "server" | awk -F ': ' '{ print $2 }' | awk -F '.' '{ print $1 }' | cut -c1-2 | tr [a-z] [A-Z])"
connlen="$(cat /usr/local/share/vpn)"

if [ "$server" == "" ] && [ "$connlen" == "0" ]; then
    if [ "$1" == "clean" ];
    then
        echo ""
    else
        echo "%{F#bf616a}"
    fi
else
    if [ "$1" == "clean" ];
    then
        echo ""
    else
        echo "%{F#a3be8c}"
    fi
fi
