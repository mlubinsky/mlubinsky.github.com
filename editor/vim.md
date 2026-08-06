## Vim


https://github.com/mhinz/vim-galore

https://www.youtube.com/watch?v=XA2WjJbmmoM

https://www.youtube.com/watch?v=wlR5gYd6um0

 
 ### csv plugin
 https://www.vim.org/scripts/script.php?script_id=2830
 
 Open csv.vmb in Vim and source the file: 
```
 :so % 
```
This will install the plugin into your $HOME/.vim/ftplugin directory and the documentation into your $HOME/.vim/doc directory. 

```
 mkdir -p ~/.vim/pack/my-plugins/start
 git clone https://github.com/chrisbra/csv.vim ~/.vim/pack/dist/start/csv
 
 :helptags
 https://github.com/chrisbra/csv.vim
```

https://news.ycombinator.com/item?id=30084913

```
:w !sudo tee "%"
```

https://github.com/chrisbra/csv.vim  CSV viewer

https://jaredgorski.org/writing/6-a-vim-puff-piece/

https://changelog.com/podcast/450

https://vim-bootstrap.com/

https://thevaluable.dev/vim-veteran/

https://thevaluable.dev/vim-expert/


### Removing trailing spaces in file

.vimrc

autocmd BufWritePre * %s/\s\+$//e



## VIM

https://www.moolenaar.net/habits.html

https://news.ycombinator.com/item?id=24363225. vim as C++ IDE

https://lobste.rs/s/du8i6z/5_lines_i_put_blank_vimrc

"| vim -" instead of less

:wq. vs :x

- custom text objects 
- vim-surround
- vim-sneak

https://www.youtube.com/watch?v=Gs1VDYnS-Ac

http://vi-essentials.palashkantikundu.in/

https://jemma.dev/blog/intermediate-vim-tips

### Plugins
1. Linting: python-mode. IMHO it provides very good linting out of the box

2. Completion: jedi-vim. Jedi for python is great!

```
  mkdir -p ~/.vim/pack/michael/start
  cd ~/.vim/pack/michael/start
  
  git clone https://tpope.io/vim/fugitive.git 
  vim -u NONE -c "helptags fugitive/doc" -c q
  
  -- gitgutter
  
  git clone https://github.com/airblade/vim-gitgutter.git
  vim -u NONE -c "helptags vim-gitgutter/doc" -c q
  --- inside vim:
  :GitGutterLineHighlightsEnable
  :set signcolumn=yes
```  

<https://news.ycombinator.com/item?id=24287566>
```
:sp/:vsp, 
can edit remote files over scp, 
:E, 
:earlier, and now 
:term, 
```


<https://stackoverflow.com/questions/1218390/what-is-your-most-productive-shortcut-with-vim/1220118#1220118>

<https://danielmiessler.com/study/vim/>

<https://www.youtube.com/watch?v=E-ZbrtoSuzw>

<https://www.youtube.com/watch?v=futay9NjOac>

<https://www.youtube.com/watch?v=SLQWQ_R4bRI&list=PLRjzjpJ02WDMJOTsrdByXynk8h0ScMK9R> 
```
%  -matching brackets

  ctrl-f scrolls down a page 
  ctrl-b scrolls up a page   
  Ctrl-d scrolls down half a page 
  ctrl-u scrolls up half a page.

^ takes you to the beginning of a line, 
$ to the end of a line
```
<https://stackoverflow.com/questions/1445992/vim-file-navigation>

<https://www.vimfromscratch.com/articles/vim-for-python/> Python

<http://liuchengxu.org/posts/use-vim-as-a-python-ide/>  Python

<https://stackoverflow.com/questions/1218390/what-is-your-most-productive-shortcut-with-vim>

<https://habr.com/ru/post/468265/>

<http://ismail.badawi.io/blog/2014/04/23/the-compositional-nature-of-vim/>

<https://www.youtube.com/watch?v=5r6yzFEXajQ> tmux+vim 

<https://www.youtube.com/watch?v=XA2WjJbmmoM> 

<https://www.youtube.com/watch?v=3TX3kV3TICU>  Autocompleteon 

<https://statico.github.io/vim3.html> 

<https://danielmiessler.com/study/vim/> 

<https://dougblack.io/words/a-good-vimrc.html> 

<https://boddy.im/vim-dev-env.html> 

<http://www.viemu.com/a-why-vi-vim.html> 

<https://curi0sity.de/en/2018/06/use-vim-as-a-simple-ide/> 

<https://github.com/morhetz/gruvbox/wiki/Installation> Color sheme gruvebox



## NeoVim
https://habr.com/ru/articles/889316/


https://habr.com/ru/company/avito/blog/682962/

https://toroid.org/modern-neovim

https://habr.com/ru/post/585222/

https://www.lunarvim.org/01-installing.html


## Vimium

<https://codefaster.substack.com/p/look-ma-no-mouse-vimium>

