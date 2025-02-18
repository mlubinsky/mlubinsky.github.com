set nu
set list
set listchars=tab:!·,trail:·
set ts=4
set visualbell
set t_vb=
set t_Co=256
syntax on
au BufNewFile,BufRead *.hql set filetype=sql
set background=dark
set nowrap
set cursorline
autocmd BufWritePre * :%s/\s\+$//e
set hlsearch
:filetype plugin on
nnoremap <buffer> <F9> :exec 'w !python' shellescape(@%, 1)<cr>
