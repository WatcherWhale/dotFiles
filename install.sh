#!/bin/sh
yay -S i3-gaps rofi xob dunst nordvpn-bin ranger gcalcli figlet feh joplin kdeconnect polybar

git clone --bare git@gitlab.com:WatcherWhale/dots.git $HOME/.dotfiles
git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME checkout

mkdir -p Projects

# Install st (simple terminal)
git clone git@gitlab.com:WatcherWhale/st.git ~/Projects/st

cd ~/Projects/st
sudo make clean install
