<https://www.smashingmagazine.com/2019/10/asynchronous-tasks-modern-javascript/>

<https://blog.soshace.com/react-and-ajax-the-art-of-fetching-data-in-react/> React + Ajax

<https://github.com/marcellomontemagno/react-ufo>

<https://habr.com/ru/post/484466/>

<https://css-tricks.com/understanding-async-await/>

<https://habr.com/ru/post/478938/>

<https://evertpot.com/await-fluent-interfaces/>

<https://developers.google.com/web/fundamentals/primers/async-functions>

<https://ponyfoo.com/articles/understanding-javascript-async-await>

<https://danlevy.net/visualizing-promises/>

<https://danlevy.net/javascript-promises-quiz/?s=r>

## Async await promises

<https://gosink.in/common-javascript-promise-mistakes-beginners/>

<https://medium.com/better-programming/callbacks-vs-promises-in-javascript-1f074e93a3b5>

<https://habr.com/ru/post/475260/>

<https://habr.com/ru/post/474726/>

<https://habr.com/ru/post/480418/>

<https://careersjs.com/magazine/async-patterns/>

<https://medium.com/dailyjs/javascript-promises-zero-to-hero-plus-cheat-sheet-64d75051cffa>
await must always be in an async function
```
 (function a() { return 'a'; })();
 // "a"

 (async function a() { return 'a'; })();
 // Promise {<resolved>: "a"}
 ```
 How to wait for end of several promisses:
 
 ```
 // Example 1:
 const arr = await Promise.all([ await1, await2 ]);
 
//Example 2:
const ids = [1, 2, 3];
const values = await Promise.all(ids.map((id) => {
return db.query('SELECT * from products WHERE id = ?', id);
}));
 ```

The following 
```
 const getUser - async name =>
   await fetch(`https://api.github.com/users/${name}`).then(r => r.json());
   
 try {
   const uset - await getUser("abcd");
 } catch (e) {
   console.log(e);
 }
```
can be expressed as:
```
  const getUser = async name =>
     await ( await fetch (`https://api.github.com/users/${name}`) ).json();
```

The Promise.all() function takes an array of promises, and returns a promise that waits for every promise in the array to resolve and then resolves to an array that contains the value each promise in the original array resolved to. 

Promise.all() is not the only way you can handle multiple async functions in parallel, there's also the Promise.race() function that executes multiple promises in parallel, waits for the first promise to resolve, and returns the value that promise resolved to.

<https://learn.javascript.ru/async-await>

<https://nikodunk.com/how-to-chain-functions-with-await-async/>

<http://thecodebarbarian.com/common-async-await-design-patterns-in-node.js.html>

<https://news.ycombinator.com/item?id=20682423>

<https://itnext.io/javascript-promises-and-async-await-as-fast-as-possible-d7c8c8ff0abc>

```
var myPromise = new Promise( 
    ( resolve, reject ) => 
         {
               resolve( 'successPayload' );
              // reject( 'errorPayload' );
         } 
);

myPromise
.then( successCallback )
.catch( errorCallback )
.finally( finallyCallback );
```

When we put async keyword before a function declaration, it becomes a promise and 
we can use await keyword inside it which blocks the code until promise it awaits resolves or rejects.
```
async function myFunction() {
   var result = await new MyPromise();
   console.log( result );
}
myFunction(); // returns a promise
```

<https://www.tutespace.com/2019/06/javascript-difference-between-promises.html> 

<https://habr.com/ru/post/462355/> 
<https://blog.patricktriest.com/what-is-async-await-why-should-you-care/> 

<https://www.youtube.com/watch?v=14hS7f8gyiw&feature=youtu.be>  
<https://101node.io/blog/how-promises-actually-work-inside-out/> 

<http://nikgrozev.com/2017/10/01/async-await/> 
<https://blog.sessionstack.com/how-javascript-works-event-loop-and-the-rise-of-async-programming-5-ways-to-better-coding-with-2f077c4438b5> 

<http://callbackhell.com/> 

<https://github.com/matt-jarrett/asynchronous-javascript-with-async-await/blob/master/README.md> 

<https://medium.com/@daspinola/javascript-from-callbacks-to-async-await-1cc090ddad99>

 JavaScript  промисы.  озволяют заменить глубокую вложенность коллбэков словом .then. 
 async-функции работают «поверх» промисов. Эти функции не представляют собой качественно другие концепции. 
  
<https://dev.to/ivanalejandro0/unraveling-callbacks-with-async-functions-5634> 

<https://blog.bitsrc.io/understanding-javascript-async-and-await-with-examples-a010b03926ea> 

<https://habr.com/ru/company/skillbox/blog/458950/>  

<https://developers.google.com/web/fundamentals/primers/async-functions> 

<https://tproger.ru/translations/understanding-async-await-in-javascript/> 

<https://www.betamark.com/blog/mistakes-using-javascript-promises/> 

<https://news.ycombinator.com/item?id=20358970> 
<https://blog.logrocket.com/handling-and-dispatching-events-with-node-js/> 


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
<https://habr.com/ru/post/472420/>

не обязательно дожидаться Promise в том же месте где вы его создали
```
const promise = fetch()
// Любой код здесь будет выполнен сразу, синхронно, не ожидая завершения fetch()
const response = await promise // ожидаем завершения promise
