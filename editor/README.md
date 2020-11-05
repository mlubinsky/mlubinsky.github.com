### Notes

<https://lobste.rs/s/e5lx5p/what_note_taking_team_wiki_personal_wiki>

## Vimium

<https://codefaster.substack.com/p/look-ma-no-mouse-vimium>

##  Latex  MathJax

<https://news.ycombinator.com/item?id=24741077>

<https://www.overleaf.com/learn>

https://www.texstudio.org/

<https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop>  Latex

## Julia + Pluto

https://www.youtube.com/watch?v=IAF8DjrQSSk

## Jupyter Book

Jupyter Book takes one or more Jupyter Notebooks and converts them into a static "book" output (looks like it primarily targets HTML output but with LaTex/PDF possible)

https://blog.jupyter.org/announcing-the-new-jupyter-book-cbf7aa8bc72e

https://news.ycombinator.com/item?id=24136955

## Linters /Formatters

<https://www.reddit.com/r/javascript/comments/cti3xs/why_you_should_use_eslint_prettier_and/>

<https://www.freecodecamp.org/news/the-guide-to-using-eslint-and-prettier-in-a-react-app/>

### Diff

<https://diffoscope.org/> 

<https://try.diffoscope.org/>

<https://marketplace.visualstudio.com/items?itemName=MadsKristensen.FileDiffer> VS Plugin

https://github.com/dandavison/delta

https://github.com/ynqa/diffy

https://github.com/ymattw/ydiff

https://github.com/so-fancy/diff-so-fancy

https://unix.stackexchange.com/questions/196565/how-to-color-diff-output

### File manager

<https://www.youtube.com/watch?v=47QYCa8AYG4> .  vifm

<https://www.youtube.com/watch?v=EGBEIb2DgtQ> . lf

<https://www.youtube.com/watch?v=cnzuzcCPYsk> nnn

## Find non-ASCII chars in file

<https://codepen.io/davidrv/full/amkWdw/>

<https://stackoverflow.com/questions/3001177/how-do-i-grep-for-all-non-ascii-characters>

 grep on OSX 10.8 no longer supports PCRE ("Perl-compatible regular expressions") 
 as Darwin now uses BSD grep instead of GNU grep.
```
grep --color='auto' -P -n "[\x80-\xFF]" file.xml
```

https://stackoverflow.com/questions/18649512/unicodedecodeerror-ascii-codec-cant-decode-byte-0xe2-in-position-13-ordinal

## Code Explorer:

<https://www.sourcetrail.com/>

## Dark mode

<https://draculatheme.com/>

## Text to Diagram

<https://www.draw.io/>

<https://news.ycombinator.com/item?id=21564990>

<https://news.ycombinator.com/item?id=21513337>

<https://avdi.codes/tools-for-turning-descriptions-into-diagrams/>

<https://news.ycombinator.com/item?id=21491715>

## MarkDown Editors: Typora, etc

<https://stackedit.io/>

<https://news.ycombinator.com/item?id=21458977>



https://news.ycombinator.com/item?id=24363225. vim as C++ IDE

## IntelliJ + Scala

<https://stackoverflow.com/questions/23545476/where-do-i-enter-the-homebrew-scala-path-usr-local-opt-scala-idea-in-intellij?rq=1>

## Diff

<https://yousseb.github.io/meld/>

<https://github.com/ymattw/ydiff>

<https://github.com/so-fancy/diff-so-fancy>

In order to make it your default Git pager, run this:

git config --global core.pager "diff-so-fancy | less --tabs=4 -RFX"

alias diff="diff-so-fancy"

## Command line tools

<https://www.vimfromscratch.com/articles/awesome-command-line-tools/>

<https://github.com/sharkdp/bat> . bat

alias cat="bat"

### Kakoune editor
https://kakoune.org/

## VIM

"| vim -" instead of less

- custom text objects 
- vim-surround
- vim-sneak

https://www.youtube.com/watch?v=Gs1VDYnS-Ac

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



## Visual Studio Code


<https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner>

<https://marketplace.visualstudio.com/items?itemName=shardulm94.trailing-spaces>

<https://habr.com/ru/company/microsoft/blog/472228/> 

<https://habr.com/ru/company/edison/blog/479828/>

<https://dev.to/lampewebdev/the-guide-to-visual-studio-code-shortcuts-higher-productivity-and-30-of-my-favourite-shortcuts-you-need-to-learn-mb3>

<https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens> . GitLens


<https://code.visualstudio.com/blogs/2019/10/03/remote-ssh-tips-and-tricks> SSH

<https://www.jonrcorbin.com/the-best-vs-code-extension-list-for-full-stack-developers/>

<https://code.visualstudio.com/docs/introvideos/debugging> . DEBUGGING


### REST extensions

<https://marketplace.visualstudio.com/items?itemName=humao.rest-client>

### VS python
<https://habr.com/ru/company/microsoft/blog/471188/> . Python extension

<https://devblogs.microsoft.com/python/python-in-visual-studio-code-january-2020-release/> Python extension


### Visual Studio Code + JavaScript

<https://www.freecodecamp.org/news/how-to-set-up-the-debugger-for-chrome-extension-in-visual-studio-code-c0b3e5937c01/>

<https://habr.com/ru/company/tinkoff/blog/461737/>

<https://medium.com/young-coder/setting-up-javascript-debugging-in-visual-studio-code-6c5005529987>

### Visual Studio Code + Scala
<https://habr.com/ru/post/469707/>

### Visual Studio Code + Java
<https://flaviocopes.com/vscode/>

<https://www.youtube.com/watch?v=sVDizUZesZk>

<https://code.visualstudio.com/docs/java/java-tutorial>

show the diff between two files, with

code --diff file1.js file2.js
 

## Other Editors 

<https://foicica.com/textadept/> 

<https://micro-editor.github.io/index.html>

<https://news.ycombinator.com/item?id=23126458>
