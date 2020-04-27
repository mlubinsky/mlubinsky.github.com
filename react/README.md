## classes
<https://jscomplete.com/learn/react-beyond-basics>

<https://app.pluralsight.com/course-player?clipId=b7748658-8609-49e9-95cf-a9b11c60a115>

<https://runjs.dev/>

<https://stackoverflow.com/questions/60795932/react-for-displaying-the-the-log-file-in-real-time-flask-backend>

## JS concepts for React
<https://kentcdodds.com/blog/javascript-to-know-for-react>

<https://codeartistry.io/10-javascript-concepts-you-need-to-master-react/>

<https://habr.com/ru/company/ruvds/blog/471040/>

<https://habr.com/ru/post/476696/> Как создать и развернуть Full-Stack React-приложение

<https://habr.com/ru/post/478750/>  plotting

## SVG in React

<https://blog.logrocket.com/how-to-use-svgs-in-react/>

## React + Chart.js + Bootstrap table

<https://github.com/trekhleb/covid-19>

<https://github.com/bgarcevic/outbreak-monitor>

<https://outbreak-monitor.herokuapp.com/>

### Dash Plotly
Github: https://github.com/cryptopotluck/Covid-19-Dash-Map

View the Application Here: https://covid-dash-udemy.herokuapp.com/

## React and D3 

<https://reactfordataviz.com/> 

<https://wattenberger.com/blog/react-and-d3>

## Docker

<https://blog.quicklyreact.com/how-to-dockerize-reactjs/>

## Ajax React 

<https://blog.soshace.com/react-and-ajax-the-art-of-fetching-data-in-react/>

## React

<https://www.youtube.com/watch?v=FNnhEBDYBr8>

<https://www.pluralsight.com/guides/working-with-bootstraps-modals-react>

<https://habr.com/ru/post/461541/> 

<https://github.com/wojtekmaj/react-lifecycle-methods-diagram>

<https://blog.logrocket.com/the-new-react-lifecycle-methods-in-plain-approachable-language-61a2105859f3/>

<https://youtu.be/2QbNCcbWDfI> Rus

<https://reactjs.org/docs/getting-started.html>

https://reactjs.org/community/examples.html

<https://youtu.be/gSvSH9tZwII> 

<https://www.taniarascia.com/getting-started-with-react/> full project with source code

<https://www.quora.com/What-are-some-good-open-source-React-JS-projects>
React example
<https://dev.to/drminnaar/11-react-examples-2e6d>

##  React Devtools for Chrome
<https://reactjs.org/blog/2019/08/15/new-react-devtools.html>

<https://medium.com/the-thinkmill/react-dev-tools-debug-like-a-ninja-c3a5d09895c6>

<https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi> 

## Udemy
<https://www.udemy.com/react-2nd-edition/> .  

## Important
<https://habr.com/ru/company/ruvds/blog/463069/>

<https://habr.com/ru/company/plarium/blog/426197/>

<https://contextneutral.com/story/react-101-things-every-beginner-should-know>


<https://habr.com/ru/post/465685/>

<http://www.theweekofreact.com/>

<https://overreacted.io/>

<https://scrimba.com/g/glearnreact>

<https://habr.com/ru/company/ruvds/blog/447134/> Russian translation

## Youtube
<https://www.youtube.com/watch?v=Ke90Tje7VS0> Learn React - React Crash Course [2019] - React Tutorial with Examples | Mosh

<https://www.youtube.com/watch?v=sBws8MSXN7A> . React JS Crash Course - 2019

<https://www.youtube.com/watch?v=DLX62G4lc44> . Learn React.js - Full Course for Beginners - Tutorial 2019

<https://youtu.be/7vo5FBzJkKY>


<https://habr.com/ru/company/hh/blog/439138/> 

<https://scotch.io/starters/react/getting-started-with-react-2019-edition>

## UseEffect and other Hooks

<https://medium.com/better-programming/8-awesome-react-hooks-2cb31aed4f3d>

<https://lukaszmakuch.pl/post/react-hooks-oops-part-1-introduction>

<https://lukaszmakuch.pl/post/react-hooks-oops-part-2-effect-runs-multiple-times-with-the-same-dependencies>

<https://lukaszmakuch.pl/post/react-hooks-oops-part-3-an-effect-does-not-run-again-when-its-dependencies-change>

<https://overreacted.io/a-complete-guide-to-useeffect/>

<https://www.robinwieruch.de/react-hooks-fetch-data>

<https://daveceddia.com/useeffect-hook-examples/>

File: Photos.js
```
import React from "react";
import { useFetch } from "./hooks";
function Photos() {
  const [data, loading] = useFetch(
    "https://jsonplaceholder.typicode.com/photos?albumId=1"
  );
  return (
    <>
      <h1>Photos</h1>
      {loading ? (
        "Loading..."
      ) : (
        <ul>
          {data.map(({ id, title, url }) => (
            <li key={`photo-${id}`}>
              <img alt={title} src={url} />
            </li>
          ))}
        </ul>
      )}
    </>
  );
}
export default Photos;
```
File: hooks.js
```
import { useState, useEffect } from "react";
function useFetch(url) {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  async function fetchUrl() {
    const response = await fetch(url);
    const json = await response.json();
    setData(json);
    setLoading(false);
  }
  useEffect(() => {
    fetchUrl();
  }, []);
  return [data, loading];
}
export { useFetch };
```

## Modal Dialog

<https://habr.com/ru/post/495518/>

For Bootstrap 3 use React-Bootstrap <https://react-bootstrap.github.io/components/modal>

```
var Modal = ReactBootstrap.Modal;
can then be used as a react component as <Modal/>.
```
For Bootstrap 4, there is react-strap <https://reactstrap.github.io>
 
<https://react-bootstrap.github.io/components/modal/>

<https://stackoverflow.com/questions/48886701/how-to-add-scroll-into-react-bootstrap-modal-body>

<https://www.pluralsight.com/guides/working-with-bootstraps-modals-react>

<https://github.com/shibe97/react-hooks-use-modal>

## useContext и useReducer в React

<https://habr.com/ru/post/473070/>

## Create-react-app

<https://github.com/facebook/create-react-app>

## Destructing objects in ES6

<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment>  

<https://css-tricks.com/new-favorite-es6-toy-destructured-objects-parameters/>
```
const o = {chico: 1, harpo: 2, groucho: 3};
const { chico, harpo, groucho } = o;  //ORDER does not matter!!
console.log(chico, harpo, groucho);
// 1 2 3


function shipmentES5Defaults(params) {
  params = params || {};
  var items =   params.items    ||   'bananas';
  var number =  params.number   ||    5;
  var pkg =     params.pkg      ||   'crates';
  console.log("We have a shipment of " + items + " in " + number + " " + pkg + ".");
}

```


## Hooks andFunctional component
<https://scotch.io/tutorials/how-to-move-from-consuming-higher-order-components-to-react-hooks>

<https://www.freecodecamp.org/news/how-to-build-a-movie-search-app-using-react-hooks-24eb72ddfaf7/>

<https://blog.bitsrc.io/11-useful-custom-react-hooks-for-your-next-app-c66307cf0f0c>

До появления хуков у функциональных компонентов не было возможности задавать локальный стейт. \
Ситуация изменилась с появлением useState().
```
const App = (props) => {
  return (
    <div>
      { props }
    </div>
  )
}
```
useState() hook:
Adding state to a functional component requires 4 steps: enabling the state, initializing, reading and updating.

<https://dmitripavlutin.com/react-usestate-hook-guide/>


## Class components and state
<https://reactjs.org/docs/react-component.html>

<https://css-tricks.com/react-state-from-the-ground-up/> \
<<https://redwerk.com/blog/core-concepts-of-state-in-react-js-and-why-to-use-it>> \
<https://github.com/uberVU/react-guide/blob/master/props-vs-state.md>

States is only available to components that are called class components.
The main reason why you will want to use class components over their counterpart, *functional components*, 
is that class components can have state.
The initial setup of state was done in the constructor, and should not be done again:
never update your component state directly.
```
class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = { username: 'johndoe' }
  }
  render() {
    const { username } = this.state
    return(
      <div>
        { username }
      </div>
    )
  }
}

```
Changing state:
```
class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = { username: 'johndoe' }
  }
  handleInputChange(username) {
    this.setState({username})
  }
  render() {
    const { username } = this.state
    return (
      <div>
        <div>
          <input 
            type="text"
            value={this.state.username}
            onChange={event => this.handleInputChange(event.target.value)}
          />
        </div>
        <p>Your username is, {username}</p>
      </div>
    )
  }
}
```
## JSX
```
const heading = <h1 className="site-heading">Hello, React</h1>
```
Using JSX is not mandatory for writing React. Under the hood, it's running createElement, which takes the tag, object containing the properties, and children of the component and renders the same information. 

The below code will have the same output as the JSX above.
```
const heading = React.createElement('h1', { className: 'site-heading' }, 'Hello, React!')
```
JSX is actually close  to JavaScript but there are a few key differences 

* className is used instead of class for adding CSS classes, as class is a reserved keyword in JavaScript.
* Properties and methods in JSX are camelCase - onclick will become onClick.
* Self-closing tags must end in a slash - e.g. ```<img />```


JavaScript expressions can also be embedded inside JSX using curly braces, including variables, functions, and properties.
```
const name = 'Tania'
const heading = <h1>Hello, {name}</h1>
```

## Props
Props (short for properties) are a Component's configuration. 
They are received from above and immutable as far as the Component receiving them is concerned.

A Component cannot change its props, 
<https://medium.com/codeiq/react-js-a-better-introduction-to-the-most-powerful-ui-library-ever-created-ecd96e8f4621> \
<https://medium.com/codeiq/mastering-react-functional-components-with-recompose-d4dd6ac98834>
Props are  parameters passed down to a component.

```
const Greetings = (props) => <div>Hey you! {props.firstName} {props.lastName}!</div>;

const App = () => (
  <div>
    <Greetings firstName="John" lastName="Smith" />
  </div>
);
```
We can further simplify the code by making use of the ES6 object destructuring syntax:

```
const Greetings = ({ firstName, lastName }) => <div>Hey you! {firstName} {lastName}!</div>;
```

```
import React from "react";

const Greetings = ({ firstName, lastName }) => (
    <div>
        Hey you! {firstName} {lastName}!
    </div>
);

export default Greetings;
```

```
import Greetings from "./Greetings";
const App = () => (
  ...
);
```
## Hooks

<https://usehooks.com/>

<https://wattenberger.com/blog/react-hooks>

<https://github.com/beautifulinteractions/beautiful-react-hooks>

<https://www.modulo.blog/jfuentes/relearning-react-with-react-hooks>

<https://www.freecodecamp.org/news/how-to-build-a-movie-search-app-using-react-hooks-24eb72ddfaf7/>

<https://dev.to/craigmichaelmartin/react-hooks-are-a-more-accurate-implementation-of-the-react-mental-model-1k49>

<https://www.netlify.com/blog/2019/03/11/deep-dive-how-do-react-hooks-really-work/>

<https://habr.com/ru/post/441722/> React Hooks

<https://habr.com/ru/company/vk/blog/454348/>

<https://www.youtube.com/watch?v=-MlNBTSg_Ww>  hooks

<https://blog.logrocket.com/frustrations-with-react-hooks/>

<https://news.ycombinator.com/item?id=20927031>

<https://blog.bitsrc.io/why-we-switched-to-react-hooks-48798c42c7f>

<https://dev.to/craigmichaelmartin/react-hooks-are-a-more-accurate-implementation-of-the-react-mental-model-1k49>

## Books
<https://leanpub.com/reintroducing-react>

<https://github.com/ohansemmanuel/Reintroducing-react>

<https://github.com/maxfarseer/react-course-ru-v2> Russian Book

## 101
<https://medium.com/codeiq/react-js-a-better-introduction-to-the-most-powerful-ui-library-ever-created-ecd96e8f4621>

<https://habr.com/ru/company/ruvds/blog/428077/> 101

<https://habr.com/ru/company/ruvds/blog/343022/> . 101

<https://habr.com/ru/company/ruvds/blog/447134/> . 28 lectures translated 

<https://github.com/30-seconds/30-seconds-of-react>

```
npx create-react-app my-app


ls my-app/
  README.md         
  node_modules      
  package-lock.json 
  package.json      
  public            
  src

cd my-app
cat public/index.html

unset HOST
npm start

At this moment go to URL: http://localhost:3000/

cat src/index.js

import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();

```
<https://jscomplete.com/>

<https://jsdrops.com/>

<https://nextjs.org/>


### Server side rendering
<https://www.youtube.com/watch?v=eenX8EGkTZM>
<https://habr.com/ru/post/473210/>
<https://blog.logrocket.com/why-you-should-render-react-on-the-server-side-a50507163b79>

```
https://www.youtube.com/playlist?list=PLUD4kD-wL_zaXhR4KU1CkUSIzh1TrvnzA#reactrally2019


https://uber.github.io/react-vis/
https://news.ycombinator.com/item?id=18562048 . Free react
https://habr.com/post/418581/
https://habr.com/company/ruvds/blog/428077/
https://medium.freecodecamp.org/these-react-fundamentals-you-skip-may-be-killing-you-7629fb87dd4a
https://tylermcginnis.com/free-react-bootcamp/
https://udilia.com/courses/learn-react-by-building-a-web-app/1
https://tylermcginnis.com/courses/
https://github.com/mattfinnell/flask-webpack-cookiecutter/
https://www.weekendjs.com/react

https://stacktrender.com/post/st/setting-up-webpack-babel-and-react-from-scratch-revisited-muffin-man
https://news.ycombinator.com/item?id=15622269
https://metanit.com/web/react/
http://css-live.ru/articles/na-osvoenie-react-mne-potrebovalas-vsego-nedelya-a-chem-vy-xuzhe.html
http://codedzen.ru/react-urok-1-osnovi/
http://websketches.ru/blog/5practiceskih-primerov-na-react

```
