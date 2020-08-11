#!/bin/sh
notih=90
res=($(xrandr | grep -w connected | grep -w primary | awk -F ' ' '{print $4}'))

height=($(echo $res | awk -F 'x' '{ print $2 }' | awk -F '+' '{ print $1 }'))
offset=($(echo $res | awk -F 'x' '{ print $2 }' | awk -F '+' '{ print $3 }'))
echo $(($height/2-$notih))"px"