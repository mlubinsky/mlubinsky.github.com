echo "hello from bash_profile"
set -o vi

export LSCOLORS=GxFxCxDxBxegedabagaced
alias ls='ls -G'
alias ll='ls -lG'

alias g='git status'
alias gd='git diff'

#### Tell grep to highlight matches
export GREP_OPTIONS='--color=auto'

#### Show Git branch in color
git_branch() {
   git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}

export PS1="[\W]\[\033[00;32m\]\$(git_branch)\[\033[00m\]\$ "
