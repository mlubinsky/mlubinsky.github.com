<https://runjs.dev/>

## React

<https://reactjs.org/docs/getting-started.html>

<https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi>  React Devtools for Chrome

<https://www.udemy.com/react-2nd-edition/>

<https://habr.com/ru/company/ruvds/blog/463069/>

<https://contextneutral.com/story/react-101-things-every-beginner-should-know>

<https://www.youtube.com/watch?v=DLX62G4lc44> . Learn React.js - Full Course for Beginners - Tutorial 2019

<https://scrimba.com/g/glearnreact>

<https://habr.com/ru/company/ruvds/blog/447134/> Russian translation

## Youtube
<https://www.youtube.com/watch?v=Ke90Tje7VS0> Learn React - React Crash Course [2019] - React Tutorial with Examples | Mosh

<https://www.youtube.com/watch?v=sBws8MSXN7A> . React JS Crash Course - 2019

<https://youtu.be/7vo5FBzJkKY>


<https://redwerk.com/blog/core-concepts-of-state-in-react-js-and-why-to-use-it>

<https://scotch.io/starters/react/getting-started-with-react-2019-edition>




## Create-react-app

<https://github.com/facebook/create-react-app>

## Destructing objects in ES6
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


## Functional component
```
const App = (props) => {
  return (
    <div>
      { props }
    </div>
  )
}
```
## Class components and state
<https://css-tricks.com/react-state-from-the-ground-up/>
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
## JSX

const heading = <h1 className="site-heading">Hello, React</h1>

Using JSX is not mandatory for writing React. Under the hood, it's running createElement, which takes the tag, object containing the properties, and children of the component and renders the same information. The below code will have the same output as the JSX above.

const heading = React.createElement('h1', { className: 'site-heading' }, 'Hello, React!')

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
https://medium.com/codeiq/react-js-a-better-introduction-to-the-most-powerful-ui-library-ever-created-ecd96e8f4621
https://medium.com/codeiq/mastering-react-functional-components-with-recompose-d4dd6ac98834
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

<https://habr.com/ru/post/441722/> React Hooks


<https://www.youtube.com/watch?v=-MlNBTSg_Ww>  hooks

## Book
<https://leanpub.com/reintroducing-react>

<https://github.com/ohansemmanuel/Reintroducing-react>


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
```
https://blog.logrocket.com/why-you-should-render-react-on-the-server-side-a50507163b79
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
https://habrahabr.ru/post/248799/
```
