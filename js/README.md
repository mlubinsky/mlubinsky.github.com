How to start python http server:

python -m SimpleHTTPServer <8000> (python2)

python3 -m http.server <8000> (python3)

http://192.168.1.2:8000

http://127.0.0.1:8000

If the directory has a file named index.html, that file will be displayed.

If there is no index.html, then the files in the directory will be listed.

<https://www.kirupa.com/tricks/billion_ways_display_svg.htm> . working with SVG


## Async await

 JavaScript  промисы.  озволяют заменить глубокую вложенность коллбэков словом .then.
  async-функции работают «поверх» промисов. Эти функции не представляют собой качественно другие концепции. 

<https://blog.bitsrc.io/understanding-javascript-async-and-await-with-examples-a010b03926ea>

<https://habr.com/ru/company/skillbox/blog/458950/>

<https://developers.google.com/web/fundamentals/primers/async-functions>

<https://tproger.ru/translations/understanding-async-await-in-javascript/>

<https://www.betamark.com/blog/mistakes-using-javascript-promises/>

<https://news.ycombinator.com/item?id=20358970>

any function called with await has to be a returning promise or created with async
```
const getData = async (url) => fetch(url);
document
  .querySelector('#submit')
  .addEventListener('click', function() { 
      // read data from DOM
      const name = document.querySelector('#name').value;
      // send to backend
      const user = await fetch(`/users?name=${name}`);
      const posts = await fetch(`/posts?userId=${user.id}`);
      const comments = await fetch(`/comments?post=${posts[0].id}`);
       
  });
```

## Web server for Chrome

<https://chrome.google.com/webstore/detail/web-server-for-chrome/ofhbbkphhbklhfoeikjpcbhemlocgigb?hl=en>

## Web workers

<https://www.twilio.com/blog/optimize-javascript-application-performance-web-workers>

<https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API>

## Visualization

https://itnext.io/javascript-real-time-visualization-of-high-frequency-streams-d6533c774794
