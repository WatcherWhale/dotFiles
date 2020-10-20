export PATH=$PATH:/home/watcherwhale/.local/bin:/home/watcherwhale/.scripts/:/opt/texlive/2020/bin/x86_64-linux/:/usr/local/MATLAB/R2020b/bin/
export EDITOR="nvim"
export DIFFPROG="nvim -d"
export TEXMFHOME="~/.local/share/texmf"
export ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=8"
export JUPYTERLAB_DIR=$HOME/.local/share/jupyter/lab
export DOTNET_CLI_TELEMETRY_OPTOUT=1

export MODE_CURSOR_VIINS="bar"

~/.scripts/terminalmsg

# Set History file
export HISTFILE=~/.config/zsh/.zsh_history

# Set Auto suggest strategy
ZSH_AUTOSUGGEST_STRATEGY=(history)

# Oh My Zsh
export ZSH="/usr/share/oh-my-zsh"

# Theming
ZSH_THEME="spaceship"

ZSH_HIGHLIGHT_HIGHLIGHTERS=(main brackets pattern cursor)
plugins=(zsh-autosuggestions zsh-syntax-highlighting zsh-completions zsh-vim-mode)

source $HOME/.config/zsh/spaceship.sh
source $ZSH/oh-my-zsh.sh

# Extract archives
ex ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1   ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *.deb)       ar x $1      ;;
      *.tar.xz)    tar xf $1    ;;
      *.tar.zst)   unzstd $1    ;;      
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

# Aliases

# use bashtop instead of htop
alias htop="bashtop"
# Make ranger cd to the chosen directory
alias ranger='ranger --choosedir=$HOME/.rangerdir; LASTDIR=`cat $HOME/.rangerdir`; cd "$LASTDIR"'

# Shorten commen commands
alias r="ranger"
alias r2="radare2 -A"
alias j="joplin"

# use trash instead of the default remove
alias rm="trash"

# Media
alias ytmp3="youtube-dl -x --audio-format mp3"
alias cpimg="xclip -selection clipboard -t image/png -i"

alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

# Vim
alias vim="nvim"
alias svim="sudo -e"

# cd aliasses
alias ..="cd .."
alias ...="cd ../.."

# mkdir & cd
function mcd
{
    command mkdir -p $1 && cd $1
}

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
alias mirrord="sudo reflector --latest 50 --number 20 --sort delay --save /etc/pacman.d/mirrorlist"
alias mirrors="sudo reflector --latest 50 --number 20 --sort score --save /etc/pacman.d/mirrorlist"
alias mirrora="sudo reflector --latest 50 --number 20 --sort age --save /etc/pacman.d/mirrorlist"

alias cat="bat"

# Fun
alias rr="~/.scripts/roll.sh"

if [ -f ~/.config/zsh/zsh-insulter/src/zsh.command-not-found ]; then
    . ~/.config/zsh/zsh-insulter/src/zsh.command-not-found
fi

# SSH Session
SSHAGENT=/usr/bin/ssh-agent
SSHAGENTARGS="-s"
if [ -z "$SSH_AUTH_SOCK" -a -x "$SSHAGENT" ]; then
    eval `$SSHAGENT $SSHAGENTARGS` > /dev/null
    trap "kill $SSH_AGENT_PID" 0
fi

# Limit History file
export SAVEHIST=1000
setopt HIST_FIND_NO_DUPS
