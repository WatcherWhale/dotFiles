#!/usr/bin/env bash

country="$(nordvpn status | grep -w "Country" | awk -F ': ' '{ print $2 }')"
city="$(nordvpn status | grep -w "City" | awk -F ': ' '{ print $2 }')"


if [ "$country" == "" ]; then
    echo "🔓 Disconnected"
else
    echo "🔐 $country: $city"
fi
