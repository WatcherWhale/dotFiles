call plug#begin('/home/watcherwhale/.config/nvim/plugged')

" Git
Plug 'tpope/vim-fugitive'
Plug 'airblade/vim-gitgutter'

" Autocomplete
Plug 'neoclide/coc.nvim', {'branch': 'release'}

" Syntax Highlighting
Plug 'sheerun/vim-polyglot'
Plug 'ap/vim-css-color'

" Lightline
Plug 'itchyny/lightline.vim'

" Nord
Plug 'arcticicestudio/nord-vim'

" Markdown
Plug 'godlygeek/tabular'
Plug 'plasticboy/vim-markdown'

Plug 'iamcco/markdown-preview.nvim', { 'do': 'cd app & yarn install' }

" Distraction free vim
Plug 'junegunn/goyo.vim'

" Nerdtree
Plug 'preservim/nerdtree'
Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
Plug 'ryanoasis/vim-devicons'
Plug 'Xuyuanp/nerdtree-git-plugin'

" Latex
Plug 'lervag/vimtex'

" Matlab
Plug 'jvirtanen/vim-octave'

" Vim Rainbow (coloured pairs)
" Plug 'frazrepo/vim-rainbow'

" Comments
Plug 'preservim/nerdcommenter'

" Fzf
Plug 'junegunn/fzf.vim'

" Documentation Generator
Plug 'kkoomen/vim-doge'

" I3 Config
Plug 'mboughaba/i3config.vim'

call plug#end()
