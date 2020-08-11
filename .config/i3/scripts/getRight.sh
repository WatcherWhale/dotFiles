#!/bin/sh
notiw=260
res=($(xrandr | grep -w connected | grep -w primary | awk -F ' ' '{print $4}'))

width=($(echo $res | awk -F 'x' '{ print $1 }'))
widthOffset=($(echo $res | awk -F '+' '{ print $2 }'))

bottom=$(($width+$widthOffset))
echo $(($width/2-$notiw))"px"