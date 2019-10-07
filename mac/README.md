<https://github.com/appalaszynski/mac-setup>

<https://dbngin.com/> . Free All-in-One Database Version Management Tool

<https://medium.com/@brunofrascino/working-with-multiple-java-versions-in-macos-9a9c4f15615a> 

<https://github.com/serhii-londar/open-source-mac-os-apps>

<https://chrome.google.com/webstore/detail/web-sniffer/ndfgffclcpdbgghfgkmooklaendohaef?hl=en> Web Sniffer Chrome extension

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

```
bash ./Anaconda3-2019.07-MacOSX-x86_64.sh

Preparing transaction: done
Executing transaction: \ b''
| WARNING conda.core.envs_manager:register_env(46): Unable to register environment. Path not writable or missing.
  environment location: /Users/miclub01/anaconda3
  registry file: /Users/miclub01/.conda/environments.txt
done
installation finished.
Do you wish the installer to initialize Anaconda3
by running conda init? [yes|no]
[yes] >>> yes
no change     /Users/miclub01/anaconda3/condabin/conda
no change     /Users/miclub01/anaconda3/bin/conda
no change     /Users/miclub01/anaconda3/bin/conda-env
no change     /Users/miclub01/anaconda3/bin/activate
no change     /Users/miclub01/anaconda3/bin/deactivate
no change     /Users/miclub01/anaconda3/etc/profile.d/conda.sh
no change     /Users/miclub01/anaconda3/etc/fish/conf.d/conda.fish
no change     /Users/miclub01/anaconda3/shell/condabin/Conda.psm1
no change     /Users/miclub01/anaconda3/shell/condabin/conda-hook.ps1
no change     /Users/miclub01/anaconda3/lib/python3.7/site-packages/xontrib/conda.xsh
no change     /Users/miclub01/anaconda3/etc/profile.d/conda.csh
modified      /Users/miclub01/.bash_profile

==> For changes to take effect, close and re-open your current shell. <==

If you'd prefer that conda's base environment not be activated on startup,
   set the auto_activate_base parameter to false:

conda config --set auto_activate_base false

Thank you for installing Anaconda3!




python -V .    Python 3.7.3
conda create --name deepCognition python=3.7.3

#
# To activate this environment, use
#
#     $ conda activate deepCognition
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(base) [arm-space-analytics](master)$ conda activate deepCognition
(deepCognition) [arm-space-analytics](master)$


conda activate deepCognition
pip -V
pip 19.1.1 from /Users/miclub01/anaconda3/envs/deepCognition/lib/python3.7/site-packages/pip (python 3.7)

```


### Color command line
<https://www.cyberciti.biz/faq/apple-mac-osx-terminal-color-ls-output-option/>
```
alias ls='ls -G'
alias ll='ls -lG'

ls -G
```
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
