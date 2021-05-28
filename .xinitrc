#!/bin/sh
#
# ~/.xinitrc
#
# Executed by startx (run your window manager from here)

if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/*; do
    [ -x "$f" ] && . "$f"
  done
  unset f
fi

#if [systemd-detect-virt = "oracle"];
#	/usr/bin/VBoxClient-all
#fi

source /etc/X11/xinit/xinitrc.d/50-systemd-user.sh

eval $(/usr/bin/gnome-keyring-daemon --start --components=pkcs11,secrets,ssh)
export SSH_AUTH_SOCK

autorandr --change
xrandr --dpi 96
xrdb /home/watcherwhale/.Xresources

export QT_QPA_PLATFORMTHEME=gtk2
export QT_SCALE_FACTOR=1
export PATH=$PATH:~/.scripts/:/usr/local/MATLAB/R2020b/bin/
export EDITOR="nvim"
export TERMINAL="st"
export BROWSER="firefox"
export DIFFPROG="nvim -d"

xsettingsd &

#exec i3
exec qtile start
#exec herbstluftwm

# Exit the tty
#exit
