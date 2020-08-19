tty="$(tty)"

if [ "$tty" = "/dev/tty1" ];
then
    startx
    exit
fi

export PATH=$PATH:~/.scripts/
export EDITOR="nvim"

~/.scripts/terminalmsg

# Set History file
HISTFILE=~/.config/zsh/.zsh_history

# Set Auto suggest strategy
ZSH_AUTOSUGGEST_STRATEGY=(history)

# Oh My Zsh
export ZSH="/usr/share/oh-my-zsh"

# Theming
ZSH_THEME="spaceship"
export ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=#4b5b69"

ZSH_HIGHLIGHT_HIGHLIGHTERS=(main brackets pattern cursor)
plugins=(zsh-autosuggestions zsh-syntax-highlighting zsh-completions)

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

alias htop="bashtop"

alias ranger='ranger --choosedir=$HOME/.rangerdir; LASTDIR=`cat $HOME/.rangerdir`; cd "$LASTDIR"'
alias r="ranger"
alias r2="radare2 -A"
alias j="joplin"

alias rm="trash"
alias cpimg="xclip -selection clipboard -t image/png -i"

alias backup="sudo sh /etc/backup-service.sh"
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

alias vim="nvim"
alias svim="sudo -e"

alias ..="cd .."
alias ...="cd ../.."

alias ls="exa -l --git"
alias lsa="exa -a -l --git"

alias lss="exa"
alias lssa="exa -a"

alias cp="cp -i"

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
