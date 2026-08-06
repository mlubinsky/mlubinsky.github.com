## Editors and Viewers, diffs   for Markdown, PDF, CSV and Parquet  

<https://micro-editor.github.io/index.html>
 

### Kate Editor
brew install kate  
https://akselmo.dev/posts/how-i-use-kate-editor/  
https://apps.kde.org/kwrite/ cross platform IDE  

Kwrite is basically Kate without any plugins. Both applications are hosted in the same repo and developed at the same time.



MacOS:  
You can change TextEdit to handle plain text: Format > Convert to plain text, or Shift + Command + T.

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


### Zed

https://www.youtube.com/watch?v=q6jACvO3L5A&pp=ygUJemVkIGhlbGl4

### Lapce 
https://lapce.dev/

### PDF tools

https://news.ycombinator.com/item?id=37993575

https://habr.com/ru/companies/globalsign/articles/758568/

https://news.ycombinator.com/item?id=37110628
 
https://smallpdf.com/ru

## Sublime

https://ohdoylerules.com/workflows/why-i-still-like-sublime-text-in-2025/

### To invoke Sublime from command line (as subl)  create symbolic link

```
sudo ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl
```

### Helix 
https://helix-editor.com/ 

https://www.youtube.com/watch?v=HcuDmSb-JBU

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

 

### Text Adept

<https://foicica.com/textadept/> 



<https://news.ycombinator.com/item?id=23126458>

https://github.com/helix-editor/helix Helix
