How to start python http server:

python -m SimpleHTTPServer <8000> (python2)

python3 -m http.server <8000> (python3)

http://192.168.1.2:8000

http://127.0.0.1:8000

If the directory has a file named index.html, that file will be displayed.

If there is no index.html, then the files in the directory will be listed.

<https://www.kirupa.com/tricks/billion_ways_display_svg.htm> . working with SVG

<https://habr.com/ru/post/460741/> ES6

var status = flight.status || "unknown";

## JS coding standarts

<https://blog.back4app.com/2019/07/22/javascript-coding-standards/>

## Array operations

<https://devinduct.com/cheatsheet/8/array-operations>

<https://medium.com/better-programming/3-different-ways-to-combine-arrays-in-javascript-b273c9225e0d>

## Immutable object
<https://ultimatecourses.com/blog/all-about-immutable-arrays-and-objects-in-javascript>

## functional programming 
<https://www.codeproject.com/Articles/5163009/Functional-Programming-In-JavaScript-By-Example>

## bind call apply
<https://medium.com/@abhikulshrestha22/difference-between-bind-call-and-apply-ffe768bbc307>

## map reduce filter
<https://medium.com/sanjagh/iterating-over-javascript-objects-declaratively-or-how-to-map-filter-and-reduce-on-objects-d179cd40d935>

## Passing function as parameters
<https://pietschsoft.com/post/2019/07/24/call-functions-in-javascript>
```
function multiply(a, b) {
    return = a * b;
}

function doMath(operation, a, b) {
    return operation(a, b);
}
var c = doMath(multiply, 6, 7);
```

## Group By

<https://dev.to/studnitz/grouping-an-array-of-objects-by-key-pnp>

## Async await

 JavaScript  промисы.  озволяют заменить глубокую вложенность коллбэков словом .then.
  async-функции работают «поверх» промисов. Эти функции не представляют собой качественно другие концепции. 
  
  <https://dev.to/ivanalejandro0/unraveling-callbacks-with-async-functions-5634>

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
