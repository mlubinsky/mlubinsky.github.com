###  Enable GitHub Pages in Your Repository
Go to your GitHub repository.
Navigate to Settings > Pages.
Under Branch, select main (or another branch where your Markdown files are).
Click Save.


###  Use Jekyll for Markdown Rendering (Optional)
GitHub Pages supports Jekyll, which can convert Markdown files into a static website.

Add a _config.yml file in your repository with:

theme: jekyll-theme-minimal  
GitHub will automatically apply the theme and generate pages.

### Access Your Website
Your site will be available at:  
https://your-username.github.io/repo-name/    
or https://your-username.github.io/ if it's a user/organization site.  

### Make code in your Markdown files appears as properly formatted code on your GitHub Pages site

1. Use Proper Code Blocks in Markdown  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  
Ensure your Markdown files use fenced code blocks (triple backticks) with language identifiers for syntax highlighting:

``` 
???python
def hello():
    print("Hello, World!")
 
This tells GitHub Pages (with Jekyll) to apply syntax highlighting.

```

 2. Enable a Jekyll Theme That Supports Code Styling 
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   
GitHub Pages automatically supports Jekyll, and many themes come with built-in syntax highlighting.

- If you haven't already, create a `_config.yml` file in your repository and set a theme:
```  
???yaml
theme: jekyll-theme-minimal
```

Alternatively, try jekyll-theme-hacker for a dark-themed look:
 
theme: jekyll-theme-hacker


3. Enable Syntax Highlighting Manually (If Needed)  
^^^^^^^^^^^^^^^^^^^^   
If your theme does not support syntax highlighting, you can enable Rouge, GitHub’s default syntax highlighter:

Add this to _config.yml:
```
markdown: kramdown
highlighter: rouge
Optionally, add a custom CSS file (assets/css/style.css) with:

 
pre {
    background-color: #f5f5f5;
    padding: 10px;
    border-radius: 5px;
    overflow-x: auto;
}
code {
    font-family: 'Courier New', monospace;
    color: #d63384;
}
```
4. Use a Custom Jekyll Theme (Optional)  
^^^^^^^^^^^  
If you want more customization, consider using Minimal Mistakes or Just the Docs, which support enhanced code formatting.



### Which language identifiers are supported after tripple backquaters?
https://github.com/rouge-ruby/rouge/wiki/List-of-supported-languages-and-lexers  

```

Commonly Supported Languages
Language	Identifier
Bash/Shell	bash, sh
C	c
C++	cpp, c++
C#	csharp, cs
CSS	css
Dockerfile	dockerfile
Go	go
HTML	html
Java	java
JavaScript	javascript, js
JSON	json
Julia	julia
Kotlin	kotlin
LaTeX	latex, tex
Markdown	markdown, md
Perl	perl, pl
PHP	php
PowerShell	powershell, ps1
Python	python, py
Ruby	ruby, rb
Rust	rust
SQL	sql
Swift	swift
TypeScript	typescript, ts
XML	xml
YAML	yaml, yml
```
