### Data Grids
https://datatables.net/

https://www.ag-grid.com/

https://news.ycombinator.com/item?id=41088013

### https://threlte.xyz/ -  3D framework for the web
Built on top of Svelte and Three.js.

 ### JS


https://eloquentjavascript.net/

https://exploringjs.com/deep-js/

https://tabulator.info/docs/   Tabulator

https://turriate.com/articles/modern-javascript-everything-you-missed-over-10-years

https://httptoolkit.tech/blog/http-encodings/

https://habr.com/ru/company/mailru/blog/557386/. debugging

https://addyosmani.com/blog/import-on-interaction/ 

https://habr.com/ru/company/macloud/blog/557422/ .  DOM manipulation

## CSS 
<https://every-layout.dev/>

https://github.com/susam/spcss  HTML template

https://news.ycombinator.com/item?id=25200702

https://news.ycombinator.com/item?id=25167928

### HTMX

htmgo.dev

https://lobste.rs/s/1uv7e4/less_htmx_is_more

https://news.ycombinator.com/item?id=41683144

https://refine.dev/blog/what-is-htmx/

https://hypermedia.systems/hypermedia-systems/

https://pycoders.com/link/12216/feed FastAPI and HTMX, the right way.

https://lassebomh.github.io/htmx-playground/

https://htmx.org/  htmx allows you to access AJAX, WebSockets and Server Sent Events directly in HTML, using attributes, so you can build modern user interfaces with the simplicity and power of hypertext

<https://web.dev/one-line-layouts/>

<https://habr.com/ru/post/500304/> Grid explained

https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript

https://exploringjs.com/impatient-js/index.html. Book

https://books.goalkicker.com/JavaScriptBook/

https://exploringjs.com/deep-js/ . Book

<https://habr.com/ru/post/472816/> JS patterns

<https://www.taniarascia.com/asynchronous-javascript-event-loop-callbacks-promises-async-await/>

<https://fullstackopen.com/en/> 

<https://habr.com/ru/post/485294/> .  NodeJS in 2020 free russian cource

<https://www.wix.engineering/post/breaking-chains-with-pipelines-in-modern-javascript>

<https://www.smashingmagazine.com/2019/11/express-es6-javascript-stack-mongodb-mongoose-servers/>

<https://objectexplorer.netlify.com/>

<https://arrayexplorer.netlify.com/>

<https://habr.com/ru/post/475074/> Введение в ECMAScript 2017 (ES8)

Primitive types: это boolean, null, undefined, Number, String, Symbol, BigInt.
```
let x = 15;
let y = "15";
console.log(x+y);//здесь происходит "склеивание"
console.log(x-y); // а здесь у нас происходит нормальное вычитание
```
<https://habr.com/ru/company/otus/blog/466873/>

console.log(x instanceof Object.prototype.constructor);
console.log(typeof(x));

Don’t use console.log(obj), use 
console.log(JSON.parse(JSON.stringify(obj))).

<https://www.manning.com/books/functional-programming-in-javascript> THE BOOK


<https://medium.com/@viacheslavlushchinskiy/javascript-objects-and-arrays-manipulation-for-rest-api-b3b59a73b618>

<https://learn.javascript.ru/>

<https://exploringjs.com/>

<https://hacks.mozilla.org/category/es6-in-depth/>

<https://itnext.io/javascript-things-newbies-should-know-e04bab10449f>

<https://habr.com/ru/post/460741/> ES6

<https://eloquentjavascript.net/>

<https://habr.com/ru/post/464023/> Kiev KPI JS course


<https://habr.com/ru/post/464163/> "this" in JS

<https://www.reddit.com/r/algorithms/comments/cqf7dl/data_structures_and_algorithms_in_javascript/>


<https://kentcdodds.com/blog/javascript-to-know-for-react>

## Spread syntax
<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax>

<https://webdevblog.ru/skazka-o-treh-tochkah-v-javascript/>

<https://www.smashingmagazine.com/2019/11/express-es6-javascript-stack-mongodb-mongoose-servers/>
```
const myObjOne = { a: 'a', b: 'b' };
const myObjTwo = { ...myObjOne }:
```

## Debouncing and throtting:

<https://www.telerik.com/blogs/debouncing-and-throttling-in-javascript>

## closure
<https://codesquery.com/javascript-closure/>

## DOM manipulation

<https://itnext.io/using-the-dom-like-a-pro-163a6c552eba>

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


## loop break issue
This won't work anyway because break only works inside a loop, not a callback.
```
var listHasPilots = false;
operatives.forEach(function (operative) {
  if (operative.pilot) {
    listHasPilots = true;
    break;   
  }
});
```
 Instead:
```
var listHasPilots = false;
for (const operative of operatives) {
  if (operative.pilot) {
    listHasPilots = true;
    break;
  }
});
```

## Destructing assignment

<https://www.smashingmagazine.com/2019/11/express-es6-javascript-stack-mongodb-mongoose-servers/>

``const { a, b } = someObject ``  is specifically saying that we expect some property ``a`` and some property ``b`` to exist within someObject


Arrays can be destructured too:
```
const myArr = [4, 3];
const [valOne, valTwo] = myArr;
```
A practical reason for array destructuring occurs with React Hooks. 
```
import React, { useState } from "react";
export default () => {
  const [buttonText, setButtonText] = useState("Default");

  return (
    <button onClick={() => setButtonText("Toggled")}>
      {buttonText}
    </button>
  );
}
```


```
const response = {
   status: 200,
   data: {}
}

// instead of response.data we get...
const {data} = response //now data references the data object directly


const objectList = [ { key: 'value' }, { key: 'value' }, { key: 'value' } ]

// instead of objectList[0], objectList[1], etc we get...
const [obj, obj1, obj2] = objectList // now each object can be referenced directly

```

## some find every
<https://medium.com/poka-techblog/simplify-your-javascript-use-some-and-find-f9fb9826ddfd>

"has" already has a meaning of "key exists in object", such as in Map.prototype.has() and Set.prototype.has(), which are equivalent to Object.prototype.hasOwnProperty().

## Immutable object
<https://ultimatecourses.com/blog/all-about-immutable-arrays-and-objects-in-javascript>

## functional programming 
<https://www.codeproject.com/Articles/5163009/Functional-Programming-In-JavaScript-By-Example>

## bind call apply
<https://medium.com/@abhikulshrestha22/difference-between-bind-call-and-apply-ffe768bbc307>

## map reduce filter
<https://medium.com/sanjagh/iterating-over-javascript-objects-declaratively-or-how-to-map-filter-and-reduce-on-objects-d179cd40d935>

<https://medium.com/@stasonmars/%D0%BF%D0%BE%D0%B4%D1%80%D0%BE%D0%B1%D0%BD%D0%BE-%D0%BF%D1%80%D0%BE-%D0%BC%D0%B5%D1%82%D0%BE%D0%B4-filter-%D0%B2-javascript-1fcb239a0d74>

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


```

## Web server for Chrome

<https://chrome.google.com/webstore/detail/web-server-for-chrome/ofhbbkphhbklhfoeikjpcbhemlocgigb?hl=en>

## Web workers

<https://www.twilio.com/blog/optimize-javascript-application-performance-web-workers>

<https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API>

## Visualization

https://itnext.io/javascript-real-time-visualization-of-high-frequency-streams-d6533c774794
