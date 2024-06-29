shellcheck -o all myshellscript.sh  : use shellcheck  to check any shell script

https://zellij.dev/

https://effective-shell.com/

https://git.einval.com/cgi-bin/gitweb.cgi?p=abcde.git;a=blob_plain;f=abcde;hb=8726dfe84907e162e4b10a23cec0832ff544c1a1

https://medium.com/@devhellomello/new-computer-setup-for-techies-2024-neovim-and-ollama-and-fish-oh-my-60cf3879bad8

https://github.com/jlevy/the-art-of-command-line

https://terminaltrove.com/list/ terminal utils

https://github.com/dbohdan/structured-text-tools

https://news.ycombinator.com/item?id=40765005 find. ls, bash discussion

https://news.ycombinator.com/item?id=36501364 Working with CSV and other formats from shell

Slice and dice logs on the command line:

https://github.com/rcoh/angle-grinder

Logfile Navigator  https://lnav.org

Render Markdown on CLI
https://github.com/charmbracelet/glow

Json analysis
https://thenybble.de/posts/json-analysis/

 stream processing 
https://www.benthos.dev/

### Clickhouse Local,  DuckDB,  Polars,  for analyzing local files (including json and parquet)

https://auxten.com/the-birth-of-chdb/

https://doc.chdb.io/#/

https://antonz.org/trying-chdb/ Clickhouse embeddable 

https://clickhouse.com/blog/extracting-converting-querying-local-files-with-sql-clickhouse-local

https://www.vantage.sh/blog/clickhouse-local-vs-duckdb

https://github.com/chdb-io/chdb  -- embedded Clockhouse in python

pip install chdb

https://dbpilot.io/changelog#embedded-clickhouse-and-standalone-duckdb-support-2023-08-31

if you had data in a format that DuckDb doesn't work with, like Protobuf, Avro, ORC, Arrow, etc. ClickHouse reads and writes data in over 70 formats

### DuckDB : 
https://duckdb.org/docs/extensions/json.html 
 select a,b,c from '*.jsonl.gz'
 
```
Start your own commands in my ~/bin/ from comma !
To remember which of my commands are available in my ~/bin/ directory 
or when simply trying to remember what some of my commands are called,
I simply type a comma followed by tab and my list of commands appears

```

### Make folder and go into it:

function ccd { mkdir -p "$1" && cd "$1" }



### convert file to lower case

tr '[:upper:]' '[:lower:]' < inputFile > outputFile


### REMOVING NEWLINES (AND REPLACING WITH SPACES)

tr '\n' ' ' < inputFile


https://dashdash.io/

https://dwmkerr.com/effective-shell-part-1-navigating-the-command-line/

https://news.ycombinator.com/item?id=31448148 new command line tools like fd, etc

### Shebang

https://scriptingosx.com/2022/04/on-env-shebangs/

https://news.ycombinator.com/item?id=31027532
First line in every bash file should be:
```
#!/usr/bin/env bash
```

list of files in current folder:

echo * | tr ' ' '\n'
 

https://github.com/onceupon/Bash-Oneliner

https://news.ycombinator.com/item?id=31250275

https://www.mulle-kybernetik.com/modern-bash-scripting/

https://arslan.io/2019/07/03/how-to-write-idempotent-bash-scripts/

https://github.com/dylanaraps/pure-bash-bible

http://mywiki.wooledge.org/BashPitfalls

https://medium.com/capital-one-tech/bashing-the-bash-replacing-shell-scripts-with-python-d8d201bc0989

### jc jq

https://blog.kellybrazil.com/2022/08/29/tutorial-rapid-script-development-with-bash-jc-and-jq/

### other scripts

https://news.ycombinator.com/item?id=32467957

###	Command line tools for productive programmers 
https://news.ycombinator.com/item?id=18483460


https://github.com/alebcay/awesome-shell#applications

https://news.ycombinator.com/item?id=21363121

https://jvns.ca/blog/2022/04/12/a-list-of-new-ish--command-line-tools/
 
https://earthly.dev/blog/command-line-tools/

https://news.ycombinator.com/item?id=27992073

https://news.ycombinator.com/item?id=31009313

### JSON

https://sqlite-utils.datasette.io/en/stable/cli.html#inserting-json-data

jq https://stedolan.github.io/jq/

https://qmacro.org/tags/jq/
 
https://plantuml.com/json

https://blog.kellybrazil.com/2021/04/12/practical-json-at-the-command-line/

https://habr.com/ru/company/timeweb/blog/561214/ JSON utilities 

https://habr.com/ru/company/otus/blog/665642/


```
#1. 
get_status() {
    curl -s -X GET $RETRIEVE_ENDPOINT \
    -H 'Content-Type: application/json' \
    -d "${JSON_DATA}" \
    | jq -r '.status' \
    | cat
}

# 2. prepare request
JSON_DATA=$(jq -n \
              --arg maestroqa_token "$MAESTROQA_TOKEN" \
              --arg export_id "$EXPORT_ID" \
              '{apiToken: $maestroqa_token, exportId: $export_id }' )

# 3. get current status ("in progress" / "complete")
STATUS="$(get_status)"
printf "STATUS=$STATUS\n"

# 4. poll every 10 seconds
while [ "$STATUS" != "complete" ]; do
  printf "STATUS=$STATUS\n"
  sleep 10
  STATUS="$(get_status)"
done
```








```
cat a.json | jq -r '.key'
```

https://github.com/antonmedv/fx

### Commandline tool for running SQL queries against JSON, CSV, Excel, Parquet, and more:
 
https://github.com/multiprocessio/dsq

https://github.com/harelba/q

https://github.com/dinedal/textql

https://github.com/roapi/roapi/tree/main/columnq-cli  SQL for  parquet, csv, arrow files

miller 

### Visidata
https://jsvine.github.io/intro-to-visidata/the-big-picture/visidata-in-60-seconds/

Unlike in most other programming languages, when you define a variable in Bash, 
you must not include spaces around the variable name.

https://blog.djy.io/10-bash-quirks-and-how-to-live-with-them/

https://stackoverflow.com/questions/68606694/how-to-grep-and-replace-this-pattern-from-command-line

https://habr.com/ru/post/590021/ how to write bash scripts

https://earthly.dev/blog/command-line-tools/

https://github.com/TaKO8Ki/awesome-alternatives-in-rust

https://lib.rs/command-line-utilities

https://news.ycombinator.com/item?id=27992073

https://habr.com/ru/company/gms/blog/553078/ . useful command-line utils


### Fzf

https://news.ycombinator.com/item?id=30736518

### looking for files on S3 with pattern = XXX
```

B=s3://your_folder_here/
aws s3 ls $B  | \
awk '{print $4}' | \
xargs -I FNAME sh -c "echo FNAME; aws s3 cp ${B}FNAME - | zgrep -i -c XXX"
```



### Remove trailing spaces
```
sed 's/[[:space:]]*$//'  a.json > b.json

```

### Process 1 line at the time
```
F=abc.txt

x=0
 
cat $F | while read line; do
  x=$(( x+1 ))
  echo $x
  echo $line | jq '.' > $x.json
done
```



### Sort by numeric column 2

sort -k2 -n file

### Group by in AWK
```
awk {'a[$2]+=$6;}END{for(i in a)print i" "a[i];}' seq_with_dev.sql.out > group.txt
```

https://www.theunixschool.com/2012/06/awk-10-examples-to-group-data-in-csv-or.html

https://github.com/harelba/q   SQL for CSV files  http://harelba.github.io/q/

https://github.com/tobimensch/termsql termSQL (python3)

### AWK - find the only records where 5th column > threshold

awk  '$5 >= 2'  i.txt

### Remove header
```
cat input.csv | sed "1 d" > noheader.csv
```
### change the column delimiter  using the tr command
```
cat input.tsv | tr "\\t" "," > input.csv

cat input.csv | tr "," "\\t" > input.tsv
```

### Determining the Number of Columns
```
cat input.csv | grep -v "^#" | awk "{print NF}" FS=, | uniq
```

https://habr.com/ru/company/ruvds/blog/567150/

https://www.redhat.com/sysadmin/bash-error-handling Bash error handling!

https://opensource.com/article/21/6/bash-config parsing config files with bash



https://github.com/ibraheemdev/modern-unix

https://darrenburns.net/posts/tools/

https://darrenburns.net/posts/command-line-tools-iv





### cron

https://lobste.rs/s/0vmkgr/how_ensure_cron_job_runs_exclusively

https://blog.majid.info/lock/

### bash

Add this to  .bash_profile to go to the latest folder:
```
cd `ls -ltr | grep '^d' | tail -1 | awk '{print $9}'` 
```
 
Use && для объединения нескольких последовательных команд 


Use ? for better error message:
```
echo openjdk-${VERSION?}
-bash: VERSION: parameter null or not set
```

https://www.cyberciti.biz/tips/bash-shell-parameter-substitution-2.html

https://lobste.rs/s/yeloyn/minimal_safe_bash_script_template.  Minimal safe bash

https://news.ycombinator.com/item?id=25428621.  Minimal safe bash

https://github.com/anordal/shellharden/blob/master/how_to_do_things_safely_in_bash.md safe bash



 <https://nikhilism.com/post/2020/mystery-knowledge-useful-tools/>
 
 https://lobste.rs/s/eprvjp/what_are_your_favorite_non_standard_cli
 
 https://lobste.rs/s/ijqptg/duf_user_friendly_alternative_df

 <https://news.ycombinator.com/item?id=23229241> .  Linux Productivity Tools (2019)   (usenix.org)
 
 <https://news.ycombinator.com/item?id=23468193>
 
 <https://zaiste.net/posts/shell-commands-rust/>
 
 <https://mywiki.wooledge.org/BashPitfalls>
 
 shellcheck !!! https://github.com/koalaman/shellcheck
 
 ### GREP
 https://github.com/Genivia/ugrep  better grep
 
 ```
-i	grep -i ':4F:AB' net_interfaces.txt	Ignores case sensitivity
-w	grep -w "connect" /var/log/syslog	Search for the full word
-A	grep -A 3 'Exception' error.log	Display 3 lines of context after matching string
-B	grep -B 4 'Exception' error.log	Display 4 lines of context before matching string
-C	grep -C 5 'Exception' error.log	Display 5 lines around matching string
-r	grep -r 'quickref.me' /var/log/nginx/	Recursive search within subdirs
-v	grep -v 'warning' /var/log/syslog	Returns all non-matching lines
-e	grep -e '^Can' space_oddity.txt	Use regex (lines starting with 'Can')
-E	grep -E 'ja(s|cks)on' filename	Extended regex (lines containing jason or jackson)
-c	grep -c 'error' /var/log/syslog	Count the number of matches
-l	grep -l 'reboot' /var/log/*	Print the name of the file(s) of matches
-o	grep -o search_string filename	Only show the matching part of the string
-n	grep -n "start" demo.txt	Show the line numbers of the matches

^ 	Beginning of line.
$ 	End of line.
^$	Empty line.
\<	Start of word.
\>	End of word.
.	Any character.
? 	Optional and can only occur once.
* 	Optional and can occur more than once.
+ 	Required and can occur more than once.
{n} 	Previous item appears exactly n times.
{n,} 	Previous item appears n times or more.
{,m} 	Previous item appears n times maximum.
{n,m} 	Previous item appears between n and m times.
[:alpha:] 	Any lower and upper case letter.
[:digit:] 	Any number.
[:alnum:] 	Any lower and upper case letter or digit.
[:space:] 	Any whites­pace.
[A-Z­a-z] 	Any lower and upper case letter.
[0-9] 	Any number.
[0-9­A-Z­a-z]	Any lower and upper case letter or digit.
```


 
Use -v to show those that do not contain “match”: grep -v match file.txt  

Use -c to count how many matches: grep -c match file.txt

Show list of files that match: grep -rl match *

Number of lines to show before and after match: grep -B 2 -A 2 match file.txt


### tr (also exists: expand and unexpand)  
```
cat geeks.txt | tr ':[space]:' '\t' > out.txt  - replace spaces with tabso
cat myfile | tr a-z A-Z > output.txt
```

 ### ENTR GAZE etc
 
 https://www.reddit.com/r/programming/comments/hbetyd/gaze_a_cli_tool_that_accelerates_your_quick_coding/
 
 
 https://github.com/wtetsu/gaze  Gaze runs a command, right after you save a file.
 
 https://jvns.ca/blog/2020/06/28/entr/
 
 https://lobste.rs/s/wjaf39/entr_rerun_your_build_when_files_change entr 
 
 
 ## Terminal shortcats
 
<https://en.wikipedia.org/wiki/GNU_Readline>

<https://ramantehlan.github.io/blog/post/terminalshortcuts/>

<https://blog.balthazar-rouberol.com/shell-productivity-tips-and-tricks.html>

<https://news.ycombinator.com/item?id=24080378>



 ```
 set -o vi
 ```
 <https://catonmat.net/ftp/bash-vi-editing-mode-cheat-sheet.pdf>
 
 
 
 
 <https://switowski.com/blog/favorite-cli-tools>
 
 
### How linux works

<https://neilkakkar.com/unix.html>

<https://likegeeks.com/linux-process-management/>

### Screen

<https://www.wagner.pp.ru/fossil/advice/doc/trunk/screen.md>

## Networking
<https://habr.com/ru/post/491540/>

## Linux tools
<https://news.ycombinator.com/item?id=22438730>

<https://news.ycombinator.com/item?id=22849208> programs which  save you hours


<https://github.com/wting/autojump> autojump


### regular expression
```
My favorite regex is /[ -~]*/, space-dash-tilde. That represents approximately A-Za-z0-9 plus punctuation and space. 
It's useful for something like `tr -d` to remove all common characters and leave all of the "oddities" 
so you can differentiate "" from “” or ... from … in things like markdown or source code.

Explanation: [ -~] is matching the range of characters† from space (32) to tilde (126), 
which is the full range of printable ASCII characters. (0–31 are various control characters, and 127 is one last control character, ␡.)

To check all non-ASCII characters, you may do [^\x00-\x7F].
Depends of the language. In Python 3, files are expected to be utf8 by default, and you can change that by adding a "# coding: <charset>" header.

In fact, it's one of the reasons it was a breaking release in the first place, 
and being able to put non-ASCII characters in strings and comments in my source code are a huge plus.

It is commonly considered a faux pas to include ‘trailing white space’ in code. 
That is, your lines should end with the line-return control characters and nothing else. 
In a regular expression, the end of the string (or line) is marked by the ‘$’ symbol, and a white-space can be indicated with ‘\s’, and a sequence of one or more white space is ‘\s+’. Thus if I search for ‘\s+$‘, I will locate all offending lines.

It is often best to avoid non-ASCII characters in source code. 
Indeed, in some cases, there is no standard way to tell the compiler about your character encoding, so non-ASCII might trigger problems. 
To check all non-ASCII characters, you may do [^\x00-\x7F].

Sometimes you insert too many spaces between a variable or an operator. Multiple spaces are fine at the start of a line, 
since they can be used for indentation, but other repeated spaces are usually in error. 
You can check for them with the expression \b\s{2,}. The \b indicate a word boundary.
I use spaces to indent my code, but I always use an even number of spaces (2, 4, 8, etc.). 
Yet I might get it wrong and insert an odd number of spaces in some places. 
To detect these cases, I use the expression ^(\s\s)*\s[^\s]. To delete the extra space, 
I can select it with look-ahead and look-behind expressions such as <(?<=^(\s\s)*)\s(?=[^\s]).

I do not want a space after the opening parenthesis nor before the closing parenthesis. 
I can check for such a case with (\(\s|\s\)). If I want to remove the spaces, 
I can detect them with a look-behind expression such as (?<=\()\s.

Suppose that I want to identify all instances of a variable, I can search for \bmyname\b. 
By using word boundaries, I ensure that I do not catch instances of the string inside other functions or variable names. 
Similarly, if I want to select all variable that end with some expression, 
I can do it with an expression like \b\w*myname\b.
```
## bash job control

<https://www.linuxjournal.com/content/job-control-bash-feature-you-only-think-you-dont-need>

Job control is what allows you to suspend jobs, move jobs from the background to the foreground, and vice versa, from the foreground to the background. Running a script with script & creates a background job. Running a script with just script creates a foreground job.

Job control consists of the following commands:

* The fg command moves a background job into the foreground.
* The bg command moves a suspended foreground job into the background.
* The jobs command shows the current list of jobs.
* The kill command can kill jobs or send signals to them.
* The disown command removes a job from the list of jobs (without killing it).
* A foreground job can be suspended by typing ^Z (Control-Z). A suspended job is temporarily stopped.

## Disable buffering
Многие консольные утилиты буферизируют stdout. Из-за этого последовательный pipe ломается. 

Некоторые утилиты поддерживают настройку буферизации: sed -u, grep --line-buffered. 

В другом случае можно использовать универсальный способ stdbuf -oL и unbuffer.

### CRON
<https://habr.com/ru/company/badoo/blog/465021/>  cron etc processes PATH
<https://habr.com/ru/company/badoo/blog/468061/> .  CRON

###  bash  

<https://github.com/dylanaraps/pure-sh-bible> common shell tasks

<https://wizardzines.com/comics/bash-errors/>

Bash Error Handling (wizardzines.com)
<https://news.ycombinator.com/item?id=24727495>

<https://blog.balthazar-rouberol.com/shell-productivity-tips-and-tricks.html>

<https://news.ycombinator.com/item?id=22975437>

shellcheck  <https://www.shellcheck.net/>

Bypass finding in hidden folders:
```
find . -type f -not -path '*/\.*' | xargs grep "docker run"
```
<http://wiki.bash-hackers.org/>


To redirect the error message to NUL:
```
   dir file.xxx 2> nul
```   
Redirect the output to one place, and the errors to another:
```
   dir file.xxx > output.msg 2> output.err
```   
Combine errors and standard output to a single file: 
Redirect the output for STDERR to STDOUT and then sending the output from STDOUT to a file:
```
   dir file.xxx 1> output.msg 2>&1
   
   cmd >>file.txt 2>&1
```

```
command 2>&1 | tee -a logfile
here -a means :  Append the output to the files rather than overwriting them.
```
<https://shellmagic.xyz/>
<http://hyperpolyglot.org/>

<https://github.com/jlevy/the-art-of-command-line>

<https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html#The-Set-Builtin>
<https://unix.stackexchange.com/questions/41571/what-is-the-difference-between-and/41595#41595> . $@ vs $*
<https://blog.yossarian.net/2020/01/23/Anybody-can-write-good-bash-with-a-little-effort>
<https://github.com/anordal/shellharden/blob/master/how_to_do_things_safely_in_bash.md>
<http://caiustheory.com/bash-script-setup/>
<http://zwischenzugs.com/2018/01/06/ten-things-i-wish-id-known-about-bash/>

   bash_ru.pdf bash manual 

```
mkdir blabla
cd !$ .  <- previous command argument
sudo !! - prev command with root priv
```

https://habr.com/company/ruvds/blog/413725/    -- arrays is bash

### what is sh -c  
https://askubuntu.com/questions/831847/what-is-the-sh-c-command
https://stackoverflow.com/questions/82256/how-do-i-use-sudo-to-redirect-output-to-a-location-i-dont-have-permission-to-wr

how-to-get-the-source-directory-of-a-bash-script-from-within-the-script-itself?
https://stackoverflow.com/questions/59895/how-to-get-the-source-directory-of-a-bash-script-from-within-the-script-itself/  

```  
#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo $DIR
echo "The script basename `basename "$0"`"
  
```
### bash func() - add to .bashrc
```
function mcd(){
   mkdir -p "$1"
   cd "$1"
}

dirinfo()
{
    du -ah "$1" | sort -rh | head -n 20
}
alias dirinfo=dirinfo()
```

```
!#/bin/bash

# function which tests what $1 exists:
function test1() { command -v "$1" >/dev/null 2>&1; }
# function which tests what $1 exists but in different way:
function test2() { type -P "$1" >/dev/null; }

function die {
  >&2 echo "Fatal: ${@}"
  exit 1
}

echo ${BASH_VERSINFO[0]}
#[[ "${BASH_VERSINFO[0]}" -lt 4 ]] && die "Bash >=4 required"

## list of programs to be checked: curl nc dig:
deps=(curl nc dig)
for dep in "${deps[@]}"; do
  echo $dep
  test1 "${dep}" || die "Missing '${dep}'"
done
  
# 2 ways to chech what program (e.g. curl) exists (type and command):  
(base) [BASH_FUNC]$ type -p curl
/Users/miclub01/anaconda3/bin/curl
(base) [BASH_FUNC]$ command -v curl
/Users/miclub01/anaconda3/bin/curl
  
```  
  
### alias 

```
alias alog="tail -f /var/log/apache2/error.log"
alias please='sudo $(fc -ln -1)'

## open file from comman line with some editor:
alias tw='open -a /Applications/TextWrangler.app'
tw /path/I/want/opened/
```

https://direnv.net/


 
1 for stdout and 2 for stderr.

```
cat foo.txt > output.txt 2>&1
time echo foo 2>&1 > file.txt
```

###  nohup 
  
```  
 nohup my_cmd > run.log 2>&1 & tail -f run.log

 nohup my_cmd 1>&2  | tee nohup.out &
```

If you check the output file nohup.out during execution 
you might notice that the outputs are not written into this file until the execution is finished. 
This happens because of output buffering. If you add the -u flag you can avoid output buffering like this:
```
nohup python -u ./test.py &
```
or by specifying a log file:
```
nohup python -u ./test.py > output.log &
```

###  Command-line tools  

https://github.com/learn-anything/command-line-tools#readme
https://www.wezm.net/technical/2019/10/useful-command-line-tools/
https://news.ycombinator.com/item?id=21363121

https://peteris.rocks/blog/htop/

https://sneak.berlin/20191011/stupid-unix-tricks/
https://news.ycombinator.com/item?id=21281025

https://kvz.io/tobuntu.html . configuring ubuntu

### CSV SQL  JSON tools

https://news.ycombinator.com/item?id=28298729

https://www.johndcook.com/blog/2019/12/31/sql-join-csv-files/
https://news.ycombinator.com/item?id=21923911 	Doing a database join with CSV files
https://news.ycombinator.com/item?id=20848581 . TSV CSV JSON command line tools
https://github.com/jolmg/cq . CQ - SQL for CSV
https://github.com/johnkerl/miller .  Miller
```
  sqlite> .mode csv
  sqlite> .header on
  sqlite> .import weight.csv weight
  sqlite> .import person.csv person
  sqlite> select * from person, weight where person.ID = weight.ID;
  ID,sex,ID,weight
  123,M,123,200
  789,F,789,155
```  
 
rq fills a similar niche as tools like awk or sed, but works with structured (Avro, JSON, ProtoBuff) data instead of text.
https://github.com/dflemstr/rq

https://github.com/johnkerl/miller Miller is like awk, sed, cut, join, and sort for name-indexed data such as CSV, TSV, and tabular JSON 
http://stedolan.github.io/jq/
 
https://github.com/BurntSushi/xsv
There is very little overlap between what xsv does and what standard Unix tools like `join` do. 
Chances are, if you're using xsv for something like this, 
then you probably can't correctly use `join` to do it because `join` does not understand the CSV format.


https://github.com/antonmedv/fx JSON viewer


  
  https://habr.com/ru/post/462045/ .  /bin /sbin /usr/local/bin /home/user/bin
  https://habr.com/ru/company/first/blog/461251/   Julia Evans slides

  https://news.ycombinator.com/item?id=17874718
  
###   Logging
  https://news.ycombinator.com/item?id=20818106 

###  kills a process given its port number (4567):
```  
  kill -9 $(lsof -ti tcp:4567)
```

  List of ports in use: 
```  
  sudo lsof -iTCP -sTCP:LISTEN -P | grep 5002
       lsof -i -P -n | grep 8000
```
  find IP:
  
    dig +short myip.opendns.com @resolver1.opendns.com
    ifconfig | grep "inet " | grep -Fv 127.0.0.1 | awk '{print $2}'


### Run a long running script, but not if another copy of it is already running.

FLOCK:
https://linux.die.net/man/1/flock 

flock(1) is not POSIX, though. mkdir(1) can be used if you absolutely want a POSIX way to manage locks. 
For example:

```
    if ! mkdir .lock; then
        printf >&2 "Already running?\\n"
        exit 1
    fi
```    
Some network file system implementation do not guarantee atomic mkdir, so you still need an extra caution with this method.


### Script to automatically run program if file timestamp changed  (ENTR)

https://jvns.ca/blog/2020/06/28/entr/

<https://stackoverflow.com/questions/18599339/python-watchdog-monitoring-file-for-changes>

 https://github.com/cortesi/modd/
 
 https://news.ycombinator.com/item?id=23698305
 
<https://www.michaelcho.me/article/using-pythons-watchdog-to-monitor-changes-to-a-directory>

https://github.com/watchexec/watchexec

<https://facebook.github.io/watchman/>

https://facebook.github.io/watchman/docs/watchman-make

https://github.com/cespare/reflex

<https://gist.github.com/davidmoreno/c049e922e41aaa94e18955b9fac5549c>

<http://z3bra.org/wendy/>

<http://blog.z3bra.org/2015/03/under-wendys-dress.html>

<https://linux.die.net/man/1/watch>

<https://linux.die.net/man/1/inotifywait>

<https://github.com/fsnotify/fsnotify> (written in Go — golang)

<https://github.com/emcrisostomo/fswatch> (written in C++)

<https://github.com/watchexec/watchexec> (written in Rust)

<http://eradman.com/entrproject/>     www.entrproject.org/ run alternative command when file changed

```
#!/usr/bin/env bash
script="$1"; shift
last_mod=0
 
while true; do
    curr_mod=$(stat -f "%m" "$script")
    if ((curr_mod != last_mod)); then
        last_mod=$curr_mod
        clear
        printf "\nOutput of %s:\n\n" "$script"
        "$script" "$@"
        script_ec=$?
        if (( $script_ec != 0 )); then
            printf "\nWARNING: %s exited with non-zero exit code %d" "$script" $script_ec >&2
        fi
        last_mod=$curr_mod
    fi
 
    sleep 1
done
 
exit 0
```
  
###  Process supervisor 
http://supervisord.org/index.html

### Memory CPU
https://habrahabr.ru/company/badoo/blog/338226/
https://blog.codecentric.de/en/2017/09/jvm-fire-using-flame-graphs-analyse-performance/
https://waterprogramming.wordpress.com/2017/06/08/profiling-c-code-with-callgrind/
https://medium.com/flawless-app-stories/debugging-swift-code-with-lldb-b30c5cf2fd49   LLDB
https://jvns.ca/blog/2017/07/05/linux-tracing-systems/
http://www.brendangregg.com/sysperfbook.html
```
top -c
free -m
```

### lsof 
https://habrahabr.ru/post/353322/    lsof


Sort processed by memory consumption
```ps aux | sort -nk 4```
Sort processed by CPU consumption
```ps aux | sort -nk 3```


https://nicolargo.github.io/glances/ computer performance in python

https://tech.marksblogg.com/top-htop-glances.html

https://github.com/iipeace/guider



 


### MS Excel  
http://supercoolpics.com/10-bystryh-fishek-v-rabote-s-microsoft-excel/



### xargs  
```
find. -name "*.png" -type f -printi0 | xargsi -0 tar -cvzf images.tar.gz
ls /etc/*.conf | xargs -i cp {} /home/likegeeks/Desktop/out
```
### Table-oriented output:  column  
```
mount | column -t
cat /etc/passwd | column -t –s :
column -t < /etc/passwd
```

### Run command till it succeed (v1):

while ! [command]; do sleep 1; done

### Run command till it succeed (v2):
```
while  sleep 1
do
   ping -c 1 google.com > /dev/null 2>&1 && break
done
```


watch df -h
nohup

###  Yes/No automation 
yes | command
yes no | command

### bash examples 
Calculation in bash:
    echo $((37 * 42))

Example of bash function:
    set -e
```
    download_command () {
        if type wget >/dev/null 2>&1; then
            echo "wget -q -O-"
        elif type curl >/dev/null 2>&1; then
            echo "curl -sL"
        else
            echo "Error: curl or wget is required" >&2
            exit 1
        fi
    }

    download=$(download_command)
    public_v4=$($download http://whatismyip.akamai.com/)
    public_v6=$($download http://ipv6.whatismyip.akamai.com/)
```

### Find union, intersection and difference 
http://blog.deadvax.net/2018/05/29/shell-magic-set-operations-with-uniq/
https://news.ycombinator.com/item?id=17183092

```
    cat a b | sort | uniq > c   # c is a union b
    cat a b | sort | uniq -d > c   # c is a intersect b
    cat a b b | sort | uniq -u > c   # c is set difference a - b
```
###  AWK  
```cat log.log | awk '{ print $1 }'```

https://earthly.dev/blog/awk-examples/

https://news.ycombinator.com/item?id=28707463

https://news.ycombinator.com/item?id=20308865 .  AWK by example
  
https://github.com/thewhitetulip/awk-anti-textbook
https://github.com/noyesno/awka compiles awk to C for speed
https://invisible-island.net/mawk/ MAWK  
  
### make  
https://learnxinyminutes.com/docs/make/

http://nuclear.mutantstargoat.com/articles/make/#writing-install-uninstall-rules

### Visidata

https://jsvine.github.io/intro-to-visidata/index.html


### System info Linux

https://habr.com/ru/company/otus/blog/581796/

cat /proc/cpuinfo | grep processor | wc -l.   # number of CPUs

cat /proc/cpuinfo | grep 'core id'

lscpu

#### https://muhammadraza.me/2022/data-oneliners/
```
To print the first column of a CSV file:
awk -F, '{print $1}' file.csv
To print the first and third columns of a CSV file:
awk -F, '{print $1 "," $3}' file.csv
To print only the lines of a CSV file that contain a specific string:
grep "string" file.csv
To sort a CSV file based on the values in the second column:
sort -t, -k2 file.csv 

To remove the first row of a CSV file (the header row):
tail -n +2 file.csv
To remove duplicates from a CSV file based on the values in the first column:
awk -F, '!seen[$1]++' file.csv
To calculate the sum of the values in the third column of a CSV file:
awk -F, '{sum+=$3} END {print sum}' file.csv
To convert a CSV file to a JSON array:
jq -R -r 'split(",") | {name:.[0],age:.[1]}' file.csv
To convert a CSV file to a SQL INSERT statement:
awk -F, '{printf "INSERT INTO table VALUES (\"%s\", \"%s\", \"%s\");\n", $1, $
```

### RIGREP https://skerritt.blog/ripgrep-cheatsheet/
```
Ripgrep search for specific file types
Problem
You want to find out where the AWS ARN 123456789012 is used. You have a mono-repo with many file types in it. You're only interested in Terraform files.

Solution globbing for file types
rg '123456789012' -g '*.tf'
This globs through all files that end with .tf (the Terraform extension) for the ARN.

Problem
You want to search for the API endpoint "localhost:4531" through all Rust files.

Solution using Ripgrep's types
Ripgrep comes with a number of filetypes built in. You can do:

rg "localhost:4531" --type rust
  or more succinctly 
rg "localhost:4531" --trust
You can find the full list of file types with ripgrep --type-list.
 

Pro tip: Do rg --type-list | rg terraform to see if your file type is supported.
Problem
You want to find where the ARN is used, but want to ignore all markdown files.

Solution using inverse type selection
rg '123456789012' --type-not markdown
Case insensitive
$ rg example

$ rg -i example
hello_blog
1:ExAmple
-i does it.
```
#### Regex support
 
```
$ rg 'fast\w+' README.md
75:  faster than both. (N.B. It is not, strictly speaking, a "drop-in" replacement
119:### Is it really faster than everything else?
Find the word fast followed by some number of other letters.
```
#### Literal string (no regex)
Ripgrep by default uses regex to search. Sometimes the word we want to find contains valid regex, so this is an issue.
```
$ rg 'hello*.'
hello_blog
3:hello.*
4:hello this is a test
```

We can search literally with:
```
$ rg -F 'hello.*'
hello_blog
3:hello.*
-F is the argument
```
#### Show lines around the found text
Sometimes we want to search for something, and we'd like context on the found text in the file.

To find 1 line before our matched text:
```
$ rg "hello" -B 1
hello_blog
2-ThisIsATest
3:hello.*
-B for before
```
To find 1 line after our matched text:
```
$ rg "hello" -A 1
hello_blog
3:hello.*
4-Disney
-A for after
```
To find 1 line before and after our text:
```
$ rg "hello" -C 1
hello_blog
2-ThisIsATest
3:hello.*
4-Disney
-C for a combination of A and B
```
#### Get statistics of a search
I use this to work out how much work it would be to go through my search.

So searching "crypto" would take a while. How about crypto in Python files? This helps me speed up finding things.

rg "crypto" --stats
.... (full output of the search)
1292 matches
1083 matched lines
232 files contained matches
36826 files searched
6296587 bytes printed
254562478 bytes searched
5.805867 seconds spent searching
1.559705 seconds

#### Exclude a directory
I do not want to search through our modules directory, only our code.

We can do this by:

$ rg crypto -g '!modules/' -g '!pypi/'
Find Files
Find all files that have the word "cluster" in them.

rg --files | rg cluster
