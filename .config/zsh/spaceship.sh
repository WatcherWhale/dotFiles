export SPACESHIP_PROMPT_ORDER=(
  user          # Username section
  dir           # Current directory section
  host          # Hostname section
  time          # Time stamps section
  git           # Git section (git_branch + git_status)
  hg            # Mercurial section (hg_branch  + hg_status)
  package       # Package version
# node          # Node.js section
  ruby          # Ruby section
  elixir        # Elixir section
  xcode         # Xcode section
  swift         # Swift section
  golang        # Go section
  php           # PHP section
  rust          # Rust section
  haskell       # Haskell Stack section
  julia         # Julia section
  docker        # Docker section
  aws           # Amazon Web Services section
  gcloud        # Google Cloud Platform section
  venv          # virtualenv section
  conda         # conda virtualenv section
  pyenv         # Pyenv section
  dotnet        # .NET section
  ember         # Ember.js section
  kubectl       # Kubectl context section
  terraform     # Terraform workspace section
#  exec_time     # Execution time
  line_sep      # Line break
  battery       # Battery level and status
  vi_mode       # Vi-mode indicator
  jobs          # Background jobs indicator
  exit_code     # Exit code section
  char          # Prompt character
)

export SPACESHIP_CHAR_COLOR_SUCCESS="blue"
export SPACESHIP_CHAR_SYMBOL=" "



export SPACESHIP_DIR_COLOR=blue

export SPACESHIP_HOST_SHOW=always
export SPACESHIP_HOST_PREFIX="@ "

export SPACESHIP_TIME_COLOR=blue
export SPACESHIP_TIME_SHOW=false
export SPACESHIP_DIR_PREFIX=""

export SPACESHIP_VI_MODE_COLOR="blue"
export SPACESHIP_VI_MODE_INSERT="פֿ"
export SPACESHIP_VI_MODE_NORMAL=""
