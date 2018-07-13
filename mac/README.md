<https://github.com/appalaszynski/mac-setup>

<https://github.com/serhii-londar/open-source-mac-os-apps>    Open source Mac OS apps

<https://github.com/RafalWilinski/s3-uploader>   Upload file to S3

https://github.com/720kb/ndm  UI for npm

https://github.com/vsaravind007/nodeScratchpad   Run JS code snippets

<https://github.com/wellsjo/JSON-Splora>  JSON manipulation


### ~/.bash_profile

    #### Tell ls to be colourful
    export CLICOLOR=1
    export LSCOLORS=Exfxcxdxbxegedabagacad
 
    #### Tell grep to highlight matches
    export GREP_OPTIONS='--color=auto'
    
    #### Show Git branch in color
    git_branch() {
       git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
    }
    
    export PS1="[\W]\[\033[00;32m\]\$(git_branch)\[\033[00m\]\$ "
