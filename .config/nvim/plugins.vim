call plug#begin('/home/watcherwhale/.config/nvim/plugged')

" Latex
Plug 'lervag/vimtex'

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
" Plug 'junegunn/goyo.vim'

" Nerdtree
Plug 'preservim/nerdtree'
Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
Plug 'ryanoasis/vim-devicons'
Plug 'Xuyuanp/nerdtree-git-plugin'

Plug 'rbgrouleff/bclose.vim'
" Plug 'francoiscabrol/ranger.vim'


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

" Undo Tree
Plug 'simnalamburt/vim-mundo'

" Fuzzy finder
Plug 'ctrlpvim/ctrlp.vim'

" CPP
Plug 'rhysd/vim-clang-format'

" LSP
Plug 'prabirshrestha/vim-lsp'

" Openhab Syntax
Plug 'cyberkov/openhab-vim'

" CamelCaseWordMoving
Plug 'chaoren/vim-wordmotion'

" Live browser
Plug 'turbio/bracey.vim', {'do': 'npm install --prefix server'}

call plug#end()
