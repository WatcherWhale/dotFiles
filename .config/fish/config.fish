set -x PATH "/sbin:/bin:/usr/local/sbin:/usr/local/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl:/home/watcherwhale/.scripts/:/home/watcherwhale/.local/bin:/opt/texlive/2020/bin/x86_64-linux/:/usr/local/MATLAB/R2020b/bin/:/var/lib/snapd/snap/bin/:~/.emacs.d/bin/"
set -x BROWSER "firefox"
set -x EDITOR "nvim"
set -x DIFFPROG "nvim -d"
set -x TEXMFHOME "~/.local/share/texmf"
set -x JUPYTERLAB_DIR $HOME/.local/share/jupyter/lab
set -x DOTNET_CLI_TELEMETRY_OPTOUT 1

source ~/.config/fish/nord.fish

set fish_greeting

# Make ranger cd to the chosen directory
#alias ranger='ranger --choosedir=$HOME/.rangerdir; set LASTDIR (cat $HOME/.rangerdir); cd "$LASTDIR"'

function ranger
    command ranger --choosedir=$HOME/.rangerdir $argv; set LASTDIR (cat $HOME/.rangerdir); cd "$LASTDIR"
end

function r
    ranger $argv
end

# Shorten commen commands
#alias r="rangercd"
alias r2="radare2 -A"
alias j="joplin"
alias 2pdf="libreoffice --headless --invisible --convert-to pdf"
alias latexcompile="latexmk -pdflatex=lualatex -f -pdf -interaction=nonstopmode"
alias fm="i3-swallow pcmanfm"

# use trash instead of the default remove
alias rm="trash"

# Media
alias ytmp3="youtube-dl -x --audio-format mp3 --embed-thumbnail --add-metadata -i -o \"%(autonumber)s %(title)s.%(ext)s\""
alias cpimg="xclip -selection clipboard -t image/png -i"

alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

alias play='i3-swallow mpv --loop'
alias playfolder='i3-swallow mpv --shuffle --loop-playlist'

# Git
alias push="git push"
alias pushall="git pushall"
alias commit="git commit"
alias pull="git pull"
alias checkout="git checkout"
alias rebase="git rebase"
alias add="git add"
alias merge="git merge"

# Vim
alias vim="nvim"
alias svim="sudo -e"

# cd aliasses
alias ..="cd .."
alias ...="cd ../.."

# Long format
alias ls="exa -l --color=always --group-directories-first"
alias lsa="exa -a -l --color=always --group-directories-first"
# Short format
alias lss="exa --color=always --group-directories-first"
alias lssa="exa -a --color=always --group-directories-first"

alias cp="cp -i"

alias :q="exit"
alias q="exit"

#get fastest mirrors in your neighborhood
alias mirror="sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist"
alias mirrord="sudo reflector --verbose --latest 50 --number 20 --protocol https --sort delay --save /etc/pacman.d/mirrorlist"
alias mirrors="sudo reflector --verbose --latest 50 --number 20 --protocol https --sort score --save /etc/pacman.d/mirrorlist"
alias mirrora="sudo reflector --verbose --latest 50 --number 20 --protocol https --sort age --save /etc/pacman.d/mirrorlist"

alias cat="bat"

alias cast="catt cast"

# Fun
alias rr="~/.scripts/roll.sh"

#terminalmsg
ponysay -o
starship init fish | source
