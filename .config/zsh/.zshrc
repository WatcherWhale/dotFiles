tty="$(tty)"

if [ "$tty" = "/dev/tty1" ];
then
    startx
    exit
fi

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
plugins=(zsh-autosuggestions zsh-syntax-highlighting)

source $HOME/.config/zsh/spaceship.sh
source $ZSH/oh-my-zsh.sh
#source $HOME/.config/zsh/spaceship.sh

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

SSHAGENT=/usr/bin/ssh-agent
SSHAGENTARGS="-s"
if [ -z "$SSH_AUTH_SOCK" -a -x "$SSHAGENT" ]; then
    eval `$SSHAGENT $SSHAGENTARGS` > /dev/null
    trap "kill $SSH_AGENT_PID" 0
fi

# Load nvm
#export NVM_DIR="$HOME/.nvm"
#[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
#[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
