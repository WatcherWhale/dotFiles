" Set mouse on
" set mouse=a

" Map other esc
imap jj <Esc>

" Leader mappings
let mapleader = "ù"

nnoremap <silent> <leader>r :source /home/watcherwhale/.config/nvim/init.vim <CR>

set scrolloff=999
nnoremap <Leader>zzz :let &scrolloff=999-&scrolloff<CR>
nnoremap <Leader>zzr :let &scrolloff=999<CR>
nnoremap <Leader>zzt :let &scrolloff=10<CR>
"nnoremap j jzz
"nnoremap k kzz

" Map the <Space> key to toggle a selected fold opened/closed.
nnoremap <silent> <Space> @=(foldlevel('.')?'za':"\<Space>")<CR>
vnoremap <Space> zf

" Keyboard shortcuts
noremap <silent> <C-S>          :update<CR>
vnoremap <silent> <C-S>         <C-C>:update<CR>
inoremap <silent> <C-S>         <C-O>:update<CR>

" Split handling
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-h> <C-w>h
nnoremap <C-l> <C-w>l

nnoremap <S-h> <C-w>>
nnoremap <S-l> <C-w><



" File manager
let g:ranger_map_keys = 0
noremap <silent> <F2>      :NERDTreeToggle<CR>
vnoremap <silent> <F2>     <C-C>:NERDTreeToggle<CR>
inoremap <silent> <F2>     <C-O>:NERDTreeToggle<CR>

noremap <silent> <C-n>      :NERDTreeToggle<CR>
vnoremap <silent> <C-n>     <C-C>:NERDTreeToggle<CR>
inoremap <silent> <C-n>     <C-O>:NERDTreeToggle<CR>

noremap <silent> <leader>m      :MarkdownPreview<CR>
vnoremap <silent> <leader>m     <C-C>:MarkdownPreview<CR>
inoremap <silent> <leader>m     <C-O>:MarkdownPreview<CR>

nnoremap <silent> <leader>v     :VimtexCompile<CR>
vnoremap <silent> <leader>v     <C-C>:VimtexCompile<CR>
inoremap <silent> <leader>v     <C-O>:VimtexCompile<CR>

nnoremap <silent> <leader>f     :%!python -m json.tool<CR>

nnoremap <silent> <leader>b     :Bracey<CR>
nnoremap <silent> <leader>B     :BraceyStop<CR>

" noremap <silent> <leader>g      :Goyo<CR>
" vnoremap <silent> <leader>g     <C-C>:Goyo<CR>
" inoremap <silent> <leader>g     <C-O>:Goyo<CR>

xmap <silent> <leader>a <Plug>(coc-codeaction-selected)
nmap <silent> <leader>a <Plug>(coc-codeaction-selected)

" Coc Snippets
" Use <C-l> for trigger snippet expand.
imap <C-l> <Plug>(coc-snippets-expand)

" Use <C-j> for jump to next placeholder, it's default of coc.nvim
let g:coc_snippet_next = '<C-j>'

" Use <C-k> for jump to previous placeholder, it's default of coc.nvim
let g:coc_snippet_prev = '<C-k>'

inoremap <silent><expr> <TAB>
      \ pumvisible() ? coc#_select_confirm() :
      \ coc#expandableOrJumpable() ? "\<C-r>=coc#rpc#request('doKeymap', ['snippets-expand-jump',''])\<CR>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

let g:coc_snippet_next = '<Tab>'

nnoremap <F5> :MundoToggle<CR>

" Remap F1

map <F1> <Esc>
imap <F1> <Esc>

" Clang
autocmd FileType c,cpp,objc nnoremap <buffer><Leader>cf :<C-u>ClangFormat<CR>
autocmd FileType c,cpp,objc vnoremap <buffer><Leader>cf :ClangFormat<CR>
