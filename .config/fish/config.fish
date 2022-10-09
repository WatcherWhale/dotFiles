set -x PATH /usr/bin /usr/local/bin /bin /sbin /usr/local/sbin /usr/bin/site_perl /usr/bin/vendor_perl /usr/bin/core_perl /home/watcherwhale/.scripts/ /home/watcherwhale/.local/bin /opt/texlive/2021/bin/x86_64-linux/ /usr/local/MATLAB/R2020b/bin/ ~/.local/share/gem/ruby/3.0.0/bin /home/watcherwhale/.linkerd2/bin /home/watcherwhale/.krew/bin
set -x BROWSER "firefox"
set -x EDITOR "nvim"
set -x DIFFPROG "nvim -d"
set -x TEXMFHOME "~/.local/share/texmf"
set -x JUPYTERLAB_DIR $HOME/.local/share/jupyter/lab
set -x DOTNET_CLI_TELEMETRY_OPTOUT 1
set -x LIBVIRT_DEFAULT_URI "qemu:///system"
set -x JAVA_HOME "/usr/lib/jvm/java-17-openjdk/"

set --unexport COLUMNS
set --unexport LINES

export TALOSCONFIG="/home/watcherwhale/.config/talos/talosconfig"

eval (dircolors -c ~/.dircolors)

#source ~/.config/fish/nord.fish

set fish_greeting

source ~/.config/fish/completions/talos.fish
source ~/.config/fish/completions/linkerd.fish
source ~/.config/fish/completions/kubectl-krew.fish

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
alias latexcompile="latexmk -pdflatex=lualatex -f -shell-escape -pdf -interaction=nonstopmode"
alias fm="thunar ."

# Ansible
alias ap="ansible-playbook"

# Kubernetes
alias kc="kubectl"
alias kcw="watch -n 0.5 kubectl"
alias kcp="kubectl get pods"
alias ktop="kubectl top pods"
alias kx="kubectx"
alias kns="kubens"
alias keit="kubectl exec -it"
alias kedit="kubectl edit"

# Docker
alias deit="docker exec -it"
alias drit="docker run --rm -it"
alias dr="docker run --rm"
alias db="docker build"
alias dfimage="docker run -v /var/run/docker.sock:/var/run/docker.sock --rm alpine/dfimage"

alias ssh="env TERM=xterm-256color ssh"

alias venvactivate="source ./.venv/bin/activate.fish"

# use trash instead of the default remove
alias rm="trash"

# Media
alias ytmp3="yt-dlp -f bestaudio -x --audio-format mp3 --embed-thumbnail --add-metadata -i -o \"%(autonumber)s %(title)s.%(ext)s\""
alias cpimg="xclip -selection clipboard -t image/png -i"

alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

alias play='devour mpv --loop'
alias playfolder='devour mpv --x11-name=music --shuffle --loop-playlist'

# Theme
alias light="/home/watcherwhale/.scripts/switch light"
alias dark="/home/watcherwhale/.scripts/switch dark"

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
alias notes="nvim \"+:VimwikiIndex\""
alias n="notes"
alias wiki="notes"

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

alias battery="acpi -i -b"

#get fastest mirrors in your neighborhood
alias mirror="sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist"
alias mirrord="sudo reflector --verbose --latest 50 --number 20 --protocol https --sort delay --save /etc/pacman.d/mirrorlist"
alias mirrors="sudo reflector --verbose --latest 50 --number 20 --protocol https --sort score --save /etc/pacman.d/mirrorlist"
alias mirrora="sudo reflector --verbose --latest 50 --number 20 --protocol https --sort age --save /etc/pacman.d/mirrorlist"

#alias cat="bat"

alias cast="catt cast"

# Kitty Alias
if test "$TERM" = "xterm-kitty"
    alias kssh="kitty +kitten ssh"
    alias pssh="kitty +kitten ssh use-python"
end

# Fun
alias rr="curl -s -L https://raw.githubusercontent.com/keroserene/rickrollrc/master/roll.sh | bash"

function fish_greeting
    terminalmsg
end

starship init fish | source

function fish_command_not_found
    set_color -o red
    shuf -n 1 ~/.config/fish/insults.txt
    set_color normal
end

#bind \cL 'clear && terminalmsg'

bind \ce edit_command_buffer
