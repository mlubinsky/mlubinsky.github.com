echo "hello from bash_profile"
set -o vi #  if you want vim binding 

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

#### zsh #####

cat ~/.zshrc

function git_branch_name()
{
  branch=$(git symbolic-ref HEAD 2> /dev/null | awk 'BEGIN{FS="/"} {print $NF}')
  if [[ $branch == "" ]];
  then
    :
  else
    echo '('$branch')'
  fi
}

# Config for prompt. PS1 synonym.
prompt='%2/%F{yellow}$(git_branch_name)%f '

