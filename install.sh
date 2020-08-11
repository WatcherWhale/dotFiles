#!/bin/sh
git clone --bare https://github.com/WatcherWhale/dots.git $HOME/.dotfiles
git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME checkout
