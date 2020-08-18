#!/bin/sh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

zsh -c 'git clone https://github.com/denysdovhan/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt"''
zsh -c 'ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"'
wget https://gitlab.com/WatcherWhale/dots/-/raw/master/.config/zsh/spaceship.sh

echo source $HOME/spaceship.sh >> $HOME/.zshrc