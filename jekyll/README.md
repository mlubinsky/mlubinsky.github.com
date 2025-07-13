https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

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


### Jekyll Supported themes:

1. jekyll-theme-minimal  
   - Clean, simple, no sidebar.

2. jekyll-theme-cayman  
   - Colorful header, ideal for personal projects or portfolios.

3. jekyll-theme-midnight  
   - Dark theme, good for blogs or documentation.

4. jekyll-theme-merlot  
   - Elegant serif typography, suited for writing-heavy sites.

5. jekyll-theme-leap-day  
   - Classic design with a sidebar.

6. jekyll-theme-slate  
   - Clean dark-on-light theme with sidebar.

7. jekyll-theme-time-machine  
   - Blog-oriented theme with post history.

8. jekyll-theme-modernist   <https://pages-themes.github.io/modernist/>  https://github.com/pages-themes/modernist
   - Minimalist theme with color blocks.

How to use:
-----------
In `_config.yml`, set:

  theme: jekyll-theme-cayman

### Access Your Website
Your site will be available at:  
https://your-username.github.io/repo-name/    
or https://your-username.github.io/ if it's a user/organization site.  


### _config.yml
```
In your Jekyll _config.yml file, this line:


kramdown:
  input: GFM
means that Kramdown (the default Markdown processor for Jekyll) is configured to use GitHub Flavored Markdown (GFM) as its input syntax.

What is GFM?
GFM stands for GitHub Flavored Markdown, which is an extended version of standard Markdown with additional features.
It is the same Markdown syntax used in GitHub README files and issues.

Features of GFM
By setting input: GFM, Jekyll enables the following enhancements:

Automatic URL Linking

Plain URLs like http://google.com are automatically converted into clickable links.
Example:
 
http://google.com
✅ Becomes: http://google.com

Fenced Code Blocks
^^^^^^^^^^^^^^^^^^^^^
Allows triple backticks (```) for defining code blocks instead of needing indentation.
 
```python
def hello():
    print("Hello, World!")
 
Strikethrough Text
^^^^^^^^^^^^^^^^^^
Supports ~~strikethrough~~ text.
 
~~This text is crossed out~~
✅ Becomes: This text is crossed out

Task Lists
^^^^^^^^^^^
Supports [ ] for incomplete tasks and [x] for completed tasks.
 
- [x] Task 1
- [ ] Task 2

Supports Markdown tables.
^^^^^^^^^^^^^^^^^^^^^^^
| Name  | Age |
|-------|-----|
| Alice | 25  |
| Bob   | 30  |

Inline HTML
^^^^^^^^^^^^
Allows embedding raw HTML inside Markdown.

Should You Keep input: GFM?
Yes! If you're writing Markdown files and want them to behave the same way as on GitHub (e.g., in README.md files),
keeping GFM enabled ensures consistency.
```
### Links

```
To make plain URLs automatically clickable in your Markdown files when rendered by Jekyll, you have a few options:

1. Use Proper Markdown Link Formatting
Markdown does not automatically convert URLs into links unless they are formatted correctly. Use one of these methods:

Option 1: Enclose the URL in Angle Brackets (<>)
^^^^^^^^^
<http://google.com>
This will render as:
👉 http://google.com

Option 2: Use Markdown Link Syntax
^^^^^^^^^^ 
[Google](http://google.com)
This will render as:
👉 Google

2. Enable Jekyll's Automatic URL Linking (Kramdown)
^^^^^^^^^^^^^^^^^^^^^^
If you want Jekyll to automatically convert plain URLs into clickable links, make sure you are using the Kramdown Markdown processor with the auto_links option enabled.

Open your _config.yml file and add:
 
markdown: kramdown
kramdown:
  parse_block_html: true
  auto_links: true
Save and push your changes.
This will automatically convert http://google.com into a clickable link.

3. Convert Plain URLs Using Liquid (Alternative)
^^^^^^^^^^^^^^^^^^^^^^^
If you don't want to modify every Markdown file, you can use a Liquid filter inside your Jekyll templates to auto-convert URLs.

In your _layouts/default.html (or relevant layout file), wrap the content with this filter:

{{ content | markdownify }}
This ensures Markdown is correctly processed before being rendered.

Final Step: Test Your Site
Commit and push your changes.
Wait for GitHub Pages to rebuild your site.
Visit your site and check if the links are now clickable.

```


### Make code in your Markdown files appears as properly formatted code with syntax highlighting on your GitHub Pages site

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

### Math formula on Jekyll
To render math formulas in your Markdown files on GitHub Pages (with Jekyll), you can use MathJax, which supports LaTeX-style math notation. Here's how to do it:

1. Use MathJax in Your Markdown Files
MathJax allows you to write math formulas using LaTeX syntax.
```
1a. Inline Math (For Small Formulas Within Text)
Use single dollar signs $...$:

Euler's formula: $e^{i\pi} + 1 = 0$
This will render as:
 

2a. Block Math (For Larger Equations)
Use double dollar signs $$...$$ on separate lines:

$$
\int_0^1 x^2 \,dx = \frac{1}{3}
$$
This will render as:

 ```

2. Enable MathJax in Jekyll
By default, Jekyll does not automatically include MathJax.  
You need to manually enable it by adding MathJax support to your _layouts/default.html or head.html.  

Option 1: Add MathJax to Your Jekyll Layout 
```
Edit _layouts/default.html (or create it if it doesn’t exist), and add this inside the <head> section:

 
<script type="text/javascript" async
  src="https://polyfill.io/v3/polyfill.min.js?features=es6">
</script>
<script type="text/javascript" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>
This will load MathJax for all pages.
```
Option 2: Load MathJax Only for Specific Pages

Instead of adding it globally, include the script only in specific Markdown files:
```
 
---
layout: default
title: Math Example
---

<script type="text/javascript" async
  src="https://polyfill.io/v3/polyfill.min.js?features=es6">
</script>
<script type="text/javascript" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>

Euler's formula: $e^{i\pi} + 1 = 0$

$$
\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}
$$
```
