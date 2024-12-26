https://penrose.ink/siggraph20.html   Math visualization

https://www.stempad.com/ math notes

https://jupyterbook.org/

https://quarto.org/  open-source scientific and technical publishing system

### fast viewer for CSV and Parquet files and SQLite and DuckDb

https://www.tadviewer.com/

https://vdt-labs.com/easy-csv-editor/

https://superintendent.app/

https://github.com/Eugene-Mark/bigdata-file-viewer

### KeenWrite editor

https://github.com/DaveJarvis/keenwrite/blob/main/docs/screenshots.md

### Lapce 
https://lapce.dev/

### PDF tools

https://news.ycombinator.com/item?id=37993575

https://habr.com/ru/companies/globalsign/articles/758568/

https://news.ycombinator.com/item?id=37110628
 
https://smallpdf.com/ru

### To invoke Sublime from command line (as subl)  create symbolic link

```
sudo ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl
```

### Helix 
https://helix-editor.com/ 

https://github.com/helix-editor/helix/releases

https://www.youtube.com/watch?v=9Zj-wiQ9_Xw

#### Nova (not free)

https://nova.app/


### PyCharm

https://habr.com/ru/post/687482/

#### Lite-xl

https://lite-xl.com/

https://lite-xl.github.io/

https://betterprogramming.pub/bored-of-vs-code-try-lite-xl-76d4cb3f8dda

#### Helix and other editors

https://news.ycombinator.com/item?id=27358479

### Removing trailing spaces in file

.vimrc

autocmd BufWritePre * %s/\s\+$//e

VS Code: whitespace trimming at file save time from settings:
 File → Preference → Settings → Text Editor → Files → (scroll down a bit) to see checkbox Trim Trailing Whitespace
 

### Personal Notes

<https://lobste.rs/s/e5lx5p/what_note_taking_team_wiki_personal_wiki>

## VIM 

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


### NeoVim

https://habr.com/ru/company/avito/blog/682962/

https://toroid.org/modern-neovim

https://habr.com/ru/post/585222/

https://www.lunarvim.org/01-installing.html


## Vimium

<https://codefaster.substack.com/p/look-ma-no-mouse-vimium>

##  Latex  MathJax Typst

https://www.texifier.com/mac

https://www.youtube.com/watch?v=u9tqwIzRZ8I Latex

https://www.reddit.com/r/math/comments/1go0knl/looking_for_good_math_typing_software/

https://typst.app/docs/guides/guide-for-latex-users/

https://github.com/typst/typst

https://imaginarytext.ca/posts/2024/pandoc-typst-tutorial/

### Lyx https://www.lyx.org/

LyX combines the power and flexibility of TeX/LaTeX with the ease of use of a graphical interface. 

https://latex-cookbook.net/

https://news.ycombinator.com/item?id=29672872

https://habr.com/ru/company/skillfactory/blog/593999/

<https://news.ycombinator.com/item?id=24741077>

<https://www.overleaf.com/learn>

https://artofproblemsolving.com/wiki/index.php/LaTeX:LaTeX_on_AoPS

https://www.texstudio.org/

<https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop>  Latex

https://www.youtube.com/watch?v=331YxgOJUGw

https://medium.com/@mathcube7

TexMacs https://www.texmacs.org/tmweb/home/welcome.en.html
```
GNU TeXmacs is a free scientific editing platform designed to create beautiful technical documents using a wysiwyg interface.

It provides a unified and user friendly framework for editing structured documents with different types of content: text, mathematics, graphics, interactive content, slides, etc.

TeXmacs can be used as a graphical front-end for many systems in computer algebra, numerical analysis, statistics, etc.
```


https://www.texmacs.org/tmweb/home/welcome.en.html


## Julia + Pluto

https://www.youtube.com/watch?v=IAF8DjrQSSk

## Jupyter Book

Jupyter Book takes one or more Jupyter Notebooks and converts them into a static "book" output (looks like it primarily targets HTML output but with LaTex/PDF possible)

https://blog.jupyter.org/announcing-the-new-jupyter-book-cbf7aa8bc72e

https://news.ycombinator.com/item?id=24136955

## Linters / Formatters

<https://www.reddit.com/r/javascript/comments/cti3xs/why_you_should_use_eslint_prettier_and/>

<https://www.freecodecamp.org/news/the-guide-to-using-eslint-and-prettier-in-a-react-app/>

### Diff

CompareIt! (Windows) WinMerge (windows)

https://github.com/dandavison/delta

<https://diffoscope.org/> 

<https://try.diffoscope.org/>

<https://marketplace.visualstudio.com/items?itemName=MadsKristensen.FileDiffer> VS Plugin

https://github.com/dandavison/delta

https://github.com/ynqa/diffy

https://github.com/ymattw/ydiff

https://github.com/so-fancy/diff-so-fancy

https://unix.stackexchange.com/questions/196565/how-to-color-diff-output

 

<https://yousseb.github.io/meld/>

<https://github.com/ymattw/ydiff>

<https://github.com/so-fancy/diff-so-fancy>

In order to make it your default Git pager, run this:

git config --global core.pager "diff-so-fancy | less --tabs=4 -RFX"

alias diff="diff-so-fancy"


### File manager

ranger 
<https://www.youtube.com/watch?v=47QYCa8AYG4> .  vifm

<https://www.youtube.com/watch?v=EGBEIb2DgtQ> . lf

<https://www.youtube.com/watch?v=cnzuzcCPYsk> nnn


### cd on quit in NNN
```
if you mean the C-g behaviour then you need to set $NNN_TMPFILE:
    nnn() {
      declare -x +g NNN_TMPFILE=$(mktemp --tmpdir $0.XXXX)
      trap "rm -f $NNN_TMPFILE" EXIT
      =nnn $@
      [ -s $NNN_TMPFILE ] && source $NNN_TMPFILE
    }
    
You can use a static file if you're sure you'll never be running more than one instance.
I'd prefer something like:

    nnn() {
      local tmp=$(mktemp --tmpdir $0.XXXX)
      trap "rm -f $tmp" EXIT
      =nnn -p $tmp $@
      [ -s $tmp ] && cd ${"$(< $tmp)":h}
    }
That will cd to the selected file's directory with enter/right, or do nothing if you simply quit. 
I guess it depends if you use it for browsing a lot or simply picking a file.
 
Pressing `!` in the target directory will open a new terminal session within nnn, with that path as working dir. 
When you `exit` you'll land in nnn again.
It's not exactly the same but close enough for me.

```

### Tools

If you like terminal productivity I recommend: 
   fzf  https://betterprogramming.pub/meet-fzf-a-fuzzy-finder-to-enhance-your-command-line-workflow-a2890f6a70f8
   Facebook path picker (aka fpp), 
   fd, 
   ripgrep, 
   lf, 
   tig

Some honorable mentions: 
 tokei, 
 hyperfine, 
 lazydocker, 
 ctop, 
 ncspot.
 bat, 
 exa, 
 percol,
 GNU dialog or zenity, 
 xsv, 
 ministat, 
 gnuplot, 
 tshark, 
 mitmproxy.
 
Plus any project from sharkdp and burntsushi and any tools recommended by Brendan Gregg.

ht editor is a personal favorite too (press F6 and go to image to get started).


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




### IntelliJ P

https://www.youtube.com/watch?v=jDHQvfAVfKc

### IntelliJ Plugins
avro and parquet viewer:

https://plugins.jetbrains.com/plugin/12281-avro-and-parquet-viewer

## IntelliJ + Scala

<https://stackoverflow.com/questions/23545476/where-do-i-enter-the-homebrew-scala-path-usr-local-opt-scala-idea-in-intellij?rq=1>


## Command line tools

<https://www.vimfromscratch.com/articles/awesome-command-line-tools/>

<https://github.com/sharkdp/bat> . bat

alias cat="bat"

### Kakoune editor
https://kakoune.org/

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


https://github.com/helix-editor/helix

## Visual Studio Code

https://habr.com/ru/companies/cdek_blog/articles/811631/

https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker Spell Checker

https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh-edit   Remote SSH

https://marketplace.visualstudio.com/items?itemName=formulahendry.docker-explorer   Docker Explorer


 𝟏𝟒 𝐕𝐒 𝐂𝐨𝐝𝐞 𝐞𝐱𝐭𝐞𝐧𝐬𝐢𝐨𝐧𝐬 every Data engineer should swear by for maximum productivity..

𝐉𝐮𝐩𝐲𝐭𝐞𝐫 (𝟖𝟓𝐌+ ⬇) - Brings interactive notebooks into VS Code, perfect for exploring datasets, running Python scripts, and testing ETL pipelines

𝐃𝐨𝐜𝐤𝐞𝐫 (𝟑𝟗𝐌+ ⬇) - Simplifies container management, making it easy to set up and manage local and remote environments for your data workflows.

𝐏𝐚𝐫𝐪𝐮𝐞𝐭 𝐕𝐢𝐞𝐰𝐞𝐫 (𝟏𝟖𝟏𝐊+ ⬇) - Enables seamless viewing of Parquet files, often used in big data workflows, directly within VS Code.

𝐑𝐚𝐢𝐧𝐛𝐨𝐰 𝐂𝐒𝐕 (𝟏𝟎𝐌+ ⬇) - Highlights and formats CSV/TSV files for easier reading, making data cleaning and validation tasks much more efficient.

𝐘𝐚𝐦𝐥 (𝟏𝟗𝐌+ ⬇) - Essential for managing YAML files used in configuration for tools like Kubernetes and Airflow, ensuring your pipeline configs stay error-free.

𝐃𝐚𝐭𝐚 𝐖𝐫𝐚𝐧𝐠𝐥𝐞𝐫(𝟓𝟖𝟕𝐊+ ⬇): It provides a rich user interface to view and analyze your data, show insightful column statistics and visualizations, and automatically generate Pandas code as you clean and transform the data.

𝐂𝐨𝐩𝐢𝐥𝐨𝐭 (𝟐𝟐𝐌+ ⬇) - Powered by AI, it assists with code generation, automating repetitive tasks like writing SQL queries or transforming datasets.

𝐏𝐲𝐥𝐚𝐧𝐜𝐞 (𝟏𝟏𝟖𝐌+ ⬇): Pylance has the ability to supercharge your Python IntelliSense experience with rich type information, helping you write better code faster.

𝐒𝐐𝐋𝐓𝐨𝐨𝐥𝐬 (𝟒.𝟔𝐌+ ⬇): A must-have for connecting to databases, running queries, and exploring schemas. Simplifies interactions with PostgreSQL, MySQL, and others for your ETL tasks.

𝐂𝐥𝐨𝐮𝐝 𝐂𝐨𝐝𝐞 (𝟏.𝟓𝐌+ ⬇) - A productivity booster for working with GCP services, especially handy for orchestrating data pipelines in Kubernetes and cloud-based data solutions.

𝐈𝐧𝐝𝐞𝐧𝐭-𝐫𝐚𝐢𝐧𝐛𝐨𝐰 (𝟗.𝟏𝐌+ ⬇): Adds color and structure to your indentation, helping to debug and navigate complex YAML and Python files.

𝐒𝐐𝐋𝐢𝐭𝐞 𝐕𝐢𝐞𝐰𝐞𝐫 (𝟏.𝟓𝐌+ ⬇): Quickly view and query SQLite files, perfect for small-scale data processing or prototyping queries.

𝐏𝐨𝐬𝐭𝐦𝐚𝐧 (𝟏.𝟐𝐌+ ⬇): Ideal for testing APIs during data ingestion and integration workflows; send, monitor, and debug API requests right in VS Code.

𝐆𝐢𝐭𝐋𝐞𝐧𝐬 (𝟑𝟔𝐌+ ⬇): Adds powerful Git features directly in VS Code, helping you version-control your data engineering pipelines and track changes effectively.


```
Find matching bracket: Cmd Shift   \
```
Shift code block left: Shift+ Tab
Shift code block left: Tab

Markdown viewer plugin

https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced

https://addons.mozilla.org/en-US/firefox/addon/markdown-viewer-chrome/ 

To invoke code from command line
```
sudo ln -s /Applications/Visual\ Studio\ Code.app/Contents/Resources/app/bin/code /usr/local/bin/code
```
Or  add this to PATH
```
~/.zprofile
# Add Visual Studio Code (code)
export PATH="\$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"
```

Git History
https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory

```
  PATH=$PATH:"/Applications/Visual Studio Code.app/Contents/Resources/app/bin"
```
<https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner>

<https://marketplace.visualstudio.com/items?itemName=shardulm94.trailing-spaces>

<https://habr.com/ru/company/microsoft/blog/472228/> 

<https://habr.com/ru/company/edison/blog/479828/>

<https://dev.to/lampewebdev/the-guide-to-visual-studio-code-shortcuts-higher-productivity-and-30-of-my-favourite-shortcuts-you-need-to-learn-mb3>

<https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens> . GitLens


https://marketplace.visualstudio.com/items?itemName=tomaszbartoszewski.avro-tools AVRO Tools


<https://code.visualstudio.com/blogs/2019/10/03/remote-ssh-tips-and-tricks> SSH

<https://www.jonrcorbin.com/the-best-vs-code-extension-list-for-full-stack-developers/>

<https://code.visualstudio.com/docs/introvideos/debugging> . DEBUGGING


### REST extensions

<https://marketplace.visualstudio.com/items?itemName=humao.rest-client>

### VS Code + python

https://neps.academy/blog/how-to-install-and-configure-python-and-vscode

<https://habr.com/ru/company/microsoft/blog/471188/> . Python extension

<https://devblogs.microsoft.com/python/python-in-visual-studio-code-january-2020-release/> Python extension


### Visual Studio Code + JavaScript

<https://www.freecodecamp.org/news/how-to-set-up-the-debugger-for-chrome-extension-in-visual-studio-code-c0b3e5937c01/>

<https://habr.com/ru/company/tinkoff/blog/461737/>

<https://medium.com/young-coder/setting-up-javascript-debugging-in-visual-studio-code-6c5005529987>

### Visual Studio Code + Scala
<https://habr.com/ru/post/469707/>

### Visual Studio Code + Java

https://code.visualstudio.com/docs/java/java-tutorial

<https://flaviocopes.com/vscode/>

<https://www.youtube.com/watch?v=sVDizUZesZk>

<https://code.visualstudio.com/docs/java/java-tutorial>

### diff
show the diff between two files, with VSCode 
add to path:
```
PATH=$PATH:"/Applications/Visual Studio Code.app/Contents/Resources/app/bin"
```
code --diff file1.js file2.js
 

## Other Editors 

<https://foicica.com/textadept/> 

<https://micro-editor.github.io/index.html>

<https://news.ycombinator.com/item?id=23126458>

https://github.com/helix-editor/helix Helix
