" Set compatibility to Vim only.
set nocompatible

set guifont=DroidSansMono\ Nerd\ Font\ 11

" Helps force plug-ins to load correctly when it is turned back on below.
filetype off

" Turn off modelines
set modelines=0

" Wrap around text when line is full
set wrap

" Vim's auto indentation feature does not work properly with text copied from
" outside of Vim. Press the <F2> key to toggle paste mode on/off.

"nnoremap <F2> :set invpaste paste?<CR>
"imap <F2> <C-O>:set invpaste paste?<CR>
"set pastetoggle=<F2>

" Uncomment below to set the max textwidth. Use a value corresponding to the
" width of your screen.
" set textwidth=79
set formatoptions=tcqrn1
set tabstop=4
set shiftwidth=4
set softtabstop=4
set expandtab
set noshiftround

" Fixes common backspace problems
set backspace=indent,eol,start

" Speed up scrolling in Vim
set ttyfast

" Status bar
set laststatus=2

" Display options
set noshowmode
set showcmd

" Highlight matching pairs of brackets. Use the '%' character to jump
" between them.
set matchpairs+=<:>

" Display different types of white spaces.
set list
set listchars=tab:›\ ,trail:•,extends:#,nbsp:.

" Show line numbers
set number

" Set status line display
set statusline=

" Encoding
set encoding=utf-8

" Highlight matching search patterns
set hlsearch

" Enable incremental search
set incsearch

" Include matching uppercase words with lowercase search term
set ignorecase

" Include only uppercase words with uppercase search term
set smartcase

" Store info from no more than 100 files at a time, 9999 lines of text,
" 100kb of data. Useful for copying large amounts of data between files.
set viminfo='100,<9999,s100

" Map the <Space> key to toggle a selected fold opened/closed.
nnoremap <silent> <Space> @=(foldlevel('.')?'za':"\<Space>")<CR>
vnoremap <Space> zf

" Keyboard shortcuts
noremap <silent> <C-S>          :update<CR>
vnoremap <silent> <C-S>         <C-C>:update<CR>
inoremap <silent> <C-S>         <C-O>:update<CR>

" Sudo Write
command! -nargs=0 Sw w !sudo tee % > /dev/null

" Markdown
"   Disable folding
let g:vim_markdown_folding_disabled = 1

" Goyo
let g:goyo_width = 120
let g:goyo_height = 35

" Nerdtree

noremap <silent> <F2>      :NERDTreeToggle<CR>
vnoremap <silent> <F2>     <C-C>:NERDTreeToggle<CR>
inoremap <silent> <F2>     <C-O>:NERDTreeToggle<CR>

noremap <silent> <C-n>      :NERDTreeToggle<CR>
vnoremap <silent> <C-n>     <C-C>:NERDTreeToggle<CR>
inoremap <silent> <C-n>     <C-O>:NERDTreeToggle<CR>

let NERDTreeQuitOnOpen=1

let vim_markdown_preview_github=1
let vim_markdown_preview_browser='Firefox'
let vim_markdown_preview_hotkey='<C-i>'

let mapleader = "ù"

noremap <silent> <leader>m      :MarkdownPreview<CR>
vnoremap <silent> <leader>m     <C-C>:MarkdownPreview<CR>
inoremap <silent> <leader>m     <C-O>:MarkdownPreview<CR>

" Remap for do codeAction of selected region
function! s:cocActionsOpenFromSelected(type) abort
  execute 'CocCommand actions.open ' . a:type
endfunction
xmap <silent> <leader>a :<C-u>execute 'CocCommand actions.open ' . visualmode()<CR>
nmap <silent> <leader>a :<C-u>set operatorfunc=<SID>cocActionsOpenFromSelected<CR>g@

" Coc Snippets
" Use <C-l> for trigger snippet expand.
imap <C-l> <Plug>(coc-snippets-expand)

" Use <C-j> for select text for visual placeholder of snippet.
vmap <C-j> <Plug>(coc-snippets-select)

" Use <C-j> for jump to next placeholder, it's default of coc.nvim
let g:coc_snippet_next = '<c-j>'

" Use <C-k> for jump to previous placeholder, it's default of coc.nvim
let g:coc_snippet_prev = '<c-k>'

" Use <C-j> for both expand and jump (make expand higher priority.)
imap <C-j> <Plug>(coc-snippets-expand-jump)

inoremap <silent><expr> <TAB>
      \ pumvisible() ? coc#_select_confirm() :
      \ coc#expandableOrJumpable() ? "\<C-r>=coc#rpc#request('doKeymap', ['snippets-expand-jump',''])\<CR>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

let g:coc_snippet_next = '<tab>'

" Latex
let g:tex_flavor = 'latex'
let g:vimtex_view_method = 'zathura'
let g:vimtex_quickfix_enabled = 0

" Joplin image attach

augroup autocom
    autocmd!
    " Executes joplin command on markdown files
    " autocmd VimLeave *.md :Joplin
augroup END

command Joplin call Joplin()
fun Joplin()
    let $PATH = expand("%:p")
    !/bin/sh -c '/home/watcherwhale/.scripts/joplin-attach ${PATH}'
endfun
