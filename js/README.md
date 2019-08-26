<https://learn.javascript.ru/>

<https://exploringjs.com/>

<https://hacks.mozilla.org/category/es6-in-depth/>

<<https://habr.com/ru/post/460741/> ES6

<https://eloquentjavascript.net/>

<https://habr.com/ru/post/464023/> Kiev KPI JS course


<https://habr.com/ru/post/464163/> "this" in JS

<https://www.reddit.com/r/algorithms/comments/cqf7dl/data_structures_and_algorithms_in_javascript/>

## Spread syntax
<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax>

## Debouncing and throtting:

<https://www.telerik.com/blogs/debouncing-and-throttling-in-javascript>



## SVG
<https://www.kirupa.com/tricks/billion_ways_display_svg.htm> . working with SVG

<https://habr.com/ru/company/yandex/blog/461571/>

<https://css-tricks.com/?s=SVG>



```
var status = flight.status || "unknown";
```
## JS coding standarts

<https://blog.back4app.com/2019/07/22/javascript-coding-standards/>

## Array operations

Array.map, Array.reduce, Array.filter, Array.sort, Object.keys, Object.values.
<https://habr.com/ru/company/plarium/blog/446902/> \
<https://zellwk.com/blog/callbacks/> \
<https://zellwk.com/blog/js-promises/> \
<https://zellwk.com/blog/es6/> \
<http://zabanaa.github.io/notes/functional-programming-and-javascript-arrays.html> \
<https://stackoverflow.com/questions/24900875/whats-the-meaning-of-an-arrow-formed-from-equals-greater-than-in-javas>

<https://news.ycombinator.com/item?id=14916731>  This in JS

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

<https://www.reddit.com/r/javascript/comments/ct6o5d/higherorder_functions_map_filter_and_reduce/>

## Passing function as parameters
<https://nick.scialli.me/first-class-functions-in-javascript/> \
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

<https://medium.com/better-programming/js-reliable-fdea261012ee>
```
// ---------------------------------------------
// lambda (fat arrow) anonymous functions
// ---------------------------------------------

const doStuff = (a, b, c) => {...}

// same as:
function doStuff(a, b, c) {
  ...
}

  
// ---------------------------------------------  
// object destructuring
// ---------------------------------------------
  
const doStuff({a, b, c}) = {
  console.log(a);
}
  
// same as:
const doStuff(params) = {
  const {a, b, c} = params;
  
  console.log(a);
} 
                              
// same as:                             
const doStuff(params) = {  
  console.log(params.a);
}

                              
// ---------------------------------------------                            
// array destructuring
// ---------------------------------------------

const [a, b] = [1, 2];
                              
// same as:
const array = [1, 2];
const a = array[0];
const b = array[1];
```

## Group By

<https://dev.to/studnitz/grouping-an-array-of-objects-by-key-pnp>



## Code
```
let arr = [2, 56, 3, 41, 0, 4, 100, 23];
let sum = arr.reduce((previous, current) => current += previous);
let sum2 = arr.reduce(function(accumulator, currentValue) { return accumulator + currentValue;});
let sum3 = values.reduce(function(sum, value){ return sum + value;}, 0);
let avg = sum / arr.length;


var min = arr.reduce(function(a, b, i, arr) {return Math.min(a,b)});
var max = arr.reduce(function(a, b, i, arr) {return Math.max(a,b)});

Standard deviation: step 1
var diffs = arr.map(function(value){
  var diff = value - avg;
  return diff;
});


var squareDiffs = values.map(function(value){
  var diff = value - avg;
  var sqr = diff * diff;
  return sqr;
});

function average(data){
  var sum = data.reduce(function(sum, value){
    return sum + value;
  }, 0);

  var avg = sum / data.length;
  return avg;
}

var avgSquareDiff = average(squareDiffs);
var stdDev = Math.sqrt(avgSquareDiff);

-------

function standardDeviation(values){
  var avg = average(values);

  var squareDiffs = values.map(function(value){
    var diff = value - avg;
    var sqrDiff = diff * diff;
    return sqrDiff;
  });

  var avgSquareDiff = average(squareDiffs);

  var stdDev = Math.sqrt(avgSquareDiff);
  return stdDev;
}

function average(data){
  var sum = data.reduce(function(sum, value){
    return sum + value;
  }, 0);

  var avg = sum / data.length;
  return avg;
}

-- old style:
var myArray = [1, 2, 3, 4, 5, 6]
var add = function (a, b) {  return a + b;};
var getTotal = function (arr) { return arr.reduce(add, 0);};
getTotal(myArray); // => 21

-- modern style :
const myArray = [1, 2, 3, 4, 5, 6]
const add = (a, b) => a + b;
const getTotal = (arr) => arr.reduce(add, 0);
getTotal(myArray); // => 21

---  reduce
const oldest = people.reduce((acc, person) =>  person.age > acc.age ? person : acc);

const data = []
for (let x = 1; x <= 100000; x++) {
  data.push({ x: x, y: Math.floor(Math.random() * (1000000)) })
}

function getMinY() {
  return data.reduce((min, p) => p.y < min ? p.y : min, data[0].y);
}
function getMaxY() {
  return data.reduce((max, p) => p.y > max ? p.y : max, data[0].y);
}

function getYs(){
  return data.map(d => d.y);
}
function getMinY(){
  return Math.min(...getYs());
}
function getMaxY(){
  return Math.max(...getYs());
}
--- another implementation
function getMinY(){
  return data.reduce((min, b) => Math.min(min, b.y), data[0].y);
}
function getMaxY(){
  return data.reduce((max, b) => Math.max(max, b.y), data[0].y);
}
----  fast implementation
function findMinMax(arr) {
  let min = arr[0].y, max = arr[0].y;

  for (let i = 1, len=arr.length; i < len; i++) {
    let v = arr[i].y;
    min = (v < min) ? v : min;
    max = (v > max) ? v : max;
  }

  return [min, max];
}


------- Array Filter ---------
 Grab unique
    [1,1,2,3,4].filter( ( item, index, array ) => array.indexOf( item ) === index )
    // => [1,2,3,4]

const adults = people.filter(person => person.age > 16);


 Flatten
    [[1,2],[3,4]].reduce( ( result, item ) => result.concat(item), [] );
    // => [1,2,3,4]

Sort   -   Array.prototype.sort destructively modifies the array
    [1,2,4,3].sort( ( a, b ) => a - b )
```
## Arrow functions
```
var a = [
  "We're up all night 'til the sun",
  "We're up all night to get some",
  "We're up all night for good fun",
  "We're up all night to get lucky"
];
```
 These two assignments are equivalent:

1) Old-school ES5 without arrow function:
```
var a2 = a.map(function(s){ return s.length });
```
2) ECMAscript 6 using arrow functions:
```
var a3 = a.map( s => s.length );
```
Both a2 and a3 will be equal to [31, 30, 31, 31]
```
var numbers = [1, 5, 10, 15];
var doubles = numbers.map((x) => {  return x * 2;});
var roots = numbers.map(Math.sqrt);
var words = ["spray", "limit", "elite", "exuberant", "destruction", "present"];
var longWords = words.filter(word => word.length > 6);
var total = [0, 1, 2, 3].reduce((sum, value) => {  return sum + value;}, 0);
// total is 6

var flattened = [[0, 1], [2, 3], [4, 5]].reduce((a, b) => {return a.concat(b);}, []);
// flattened is [0, 1, 2, 3, 4, 5]

```

## Async await promises

<https://learn.javascript.ru/async-await>

<https://nikodunk.com/how-to-chain-functions-with-await-async/>

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

<https://www.tutespace.com/2019/06/javascript-difference-between-promises.html> \
<https://habr.com/ru/post/462355/> \
<https://blog.patricktriest.com/what-is-async-await-why-should-you-care/> \
<https://www.youtube.com/watch?v=14hS7f8gyiw&feature=youtu.be> \
<https://101node.io/blog/how-promises-actually-work-inside-out/> \
<http://nikgrozev.com/2017/10/01/async-await/> \
<https://blog.sessionstack.com/how-javascript-works-event-loop-and-the-rise-of-async-programming-5-ways-to-better-coding-with-2f077c4438b5> \
<http://callbackhell.com/> \
<https://github.com/matt-jarrett/asynchronous-javascript-with-async-await/blob/master/README.md> \
<https://medium.com/@daspinola/javascript-from-callbacks-to-async-await-1cc090ddad99>

 JavaScript  промисы.  озволяют заменить глубокую вложенность коллбэков словом .then. 
 async-функции работают «поверх» промисов. Эти функции не представляют собой качественно другие концепции. 
  
<https://dev.to/ivanalejandro0/unraveling-callbacks-with-async-functions-5634> \
<https://blog.bitsrc.io/understanding-javascript-async-and-await-with-examples-a010b03926ea> \
<https://habr.com/ru/company/skillbox/blog/458950/>  \
<https://developers.google.com/web/fundamentals/primers/async-functions> \
<https://tproger.ru/translations/understanding-async-await-in-javascript/> \
<https://www.betamark.com/blog/mistakes-using-javascript-promises/> \
<https://news.ycombinator.com/item?id=20358970> \
<https://blog.logrocket.com/handling-and-dispatching-events-with-node-js/> \

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
