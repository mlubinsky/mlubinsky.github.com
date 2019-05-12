<https://github.com/appalaszynski/mac-setup>

<https://dbngin.com/> . Free All-in-One Database Version Management Tool



<https://zenworkpro.com/2018/08/14/computer-ergonomics-useful-tips-for-working-in-macos>

<https://github.com/serhii-londar/open-source-mac-os-apps>    Open source Mac OS apps

<https://www.mediaatelier.com/CheatSheet/>

<https://github.com/RafalWilinski/s3-uploader>   Upload file to S3

https://github.com/720kb/ndm  UI for npm

https://github.com/vsaravind007/nodeScratchpad   Run JS code snippets

<https://github.com/wellsjo/JSON-Splora>  JSON manipulation

### Anaconda on Mac:

<https://stackoverflow.com/questions/45684618/having-default-mac-python-2-7-and-anaconda-python-3>

<https://towardsdatascience.com/how-to-successfully-install-anaconda-on-a-mac-and-actually-get-it-to-work-53ce18025f97>


### Color command line
<https://www.cyberciti.biz/faq/apple-mac-osx-terminal-color-ls-output-option/>

ls -G

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
