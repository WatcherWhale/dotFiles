#!/bin/sh
res=($(xrandr | grep -w connected | grep -w primary | awk -F ' ' '{print $4}'))
offset=($(echo $res | awk -F 'x' '{ print $2 }' | awk -F '+' '{ print $3 }'))
echo $offset"px"