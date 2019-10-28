## Books

<https://knowledgeisle.com/wp-content/uploads/2019/10/Serious-Python_-2019.pdf> Serious Python

<https://effectivepython.com/2019/10/22/memoryview-bytearray-zero-copy-interactions>  Effective Python 2nd ed

<https://www.amazon.com/Pro-Python-Features-Professional-Development-ebook/dp/B07PQBH4LL/>

<https://www.amazon.com/gp/product/1617295981>   Classic Computer Science Problems in Python

<https://habr.com/ru/company/piter/blog/471520/> Книга «Классические задачи Computer Science на языке Python»

## Use Jinja template to generate dynamic SQL
<https://medium.com/analytics-and-data/jinja-the-sql-way-of-the-ninja-9a64fc815564>

## Parsing
<https://tomassetti.me/parsing-in-python/> Parsing in Python

## multiprocessing vs threading

<http://pljung.de/posts/easy-concurrency-in-python/> . concurrency

multiprocessing vs threading
<https://sumit-ghosh.com/articles/multiprocessing-vs-threading-python-data-science/>


## Other topics

<https://habr.com/ru/company/ruvds/blog/472858/> request

<https://pydantic-docs.helpmanual.io/> . data validation

<https://kanoki.org/2019/10/16/python-logging/> . logging

<https://news.python.sc/> daily feed

<https://dev.libreneitor.com/expert-python-topics-you-should-know/>

<https://www.blog.duomly.com/20-essential-python-tips-and-tricks-you-should-know/>

<https://pysnakeblog.blogspot.com/>

<https://blog.richard.do/2019/10/17/supercharge-your-python-testing-workflow/> . Testing

<https://habr.com/ru/post/471618/> C++ fropm python

## Python tools
pyenv, poetry, black, flake8, isort, pre-commit, pytest, coverage, tox, Azure Pipelines, sphinx, and readthedocs:

<https://medium.com/georgian-impact-blog/python-tooling-makes-a-project-tick-181d567eea44>

## Import

<https://www.pythonforthelab.com/blog/complete-guide-to-imports-in-python-absolute-relative-and-more/>

## defaultdict

Task: group words by their 1st letter.
The structure we’re looking for here is a dictionary of lists, 
having the initials as key and a list of words as value, something like this:
```
{
	"a": ["all", "although", "average"],
	"b": ["best", "both"],
    ...
}
```
Solution without defaultdict
```
text = 'a long text but very interesting and fun'

data = {}
# Cycle through each word, appending it to the correct list
for word in text.split(" "):
    if word[0] in data:
        data[word[0]].append(word)
    else:
        data[word[0]] = [word]
```
Solution without defaultdict:
we completely removed the if check  because we replaced the dictionary with a defaultdict, 
specifying list as the default value ( meaning an empty list ).
```
from collections import defaultdict
text = 'a long text but very interesting and fun'

data = defaultdict(list)
# Cycle through each word, appending it to the correct list
for word in text.split(" "):
    data[word[0]].append(word)
```
## Counter
 count the number of occurrences of each word in a text. With the Counter class, this is easily accomplished:
```
from collections import Counter
text = 'and another long text but interesting and fun'

c = Counter()
for word in text.split(" "):
  c[word] += 1
print(c)
```
Actually we can do even better using the Counter’s constructor:
```
from collections import Counter
text = 'and another long text but interesting and fun'
c = Counter(text.split(" "))
print(c)
```
The most_common method: Print the 3 most common words, along with their count
```
print(c.most_common(3))
```

<https://gto76.github.io/python-cheatsheet/>

<https://github.com/sharpden/python-infrastructure>

<https://seddonym.me/2019/08/03/ioc-techniques/> inversion of control

How to start python http server:

python -m SimpleHTTPServer <8000> (python2)

python3 -m http.server <8000> (python3)



<https://habr.com/ru/post/426277/>

<https://habr.com/ru/post/457348/> . deploying from github to PythonAnyware

<https://www.techrepublic.com/google-amp/article/how-netflix-uses-python-streaming-giant-reveals-its-programming-language-libraries-and-frameworks/>

<https://habr.com/ru/post/462179/> f-strings (Python > 3.6)

<https://www.blog.duomly.com/20-essential-python-tips-and-tricks-you-should-know/>


```
from jinja2 import Template
template = Template('Hello {{ name }}!')
x=template.render(name='John Doe')
print(x)

template2 = Template(
"""
Static  begin
<ul>
{% for user in users %}
 x= {{ user.x }}
 y= {{ user.y }}
{% endfor %}
Static end
"""
)

m_users=list()

user1={
 "x": 22,
 "y": 10,
  "pose": "sitting",
}
user2={
 "x": 220,
 "y": 100,
  "pose": "sitting",
}
m_users.append(user1)
m_users.append(user2)

print (user1)
print (user2)


y=template2.render(users = m_users)
print(y)
```

