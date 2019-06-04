## Books
<https://jscomplete.com/learn/node-beyond-basics>

<<https://flaviocopes.com/> JS, Node, Express, React books>


## HTPP Server
```
ls node_modules/http-server/
ls node_modules/.bin/
./node_modules/.bin/http-server -a localhost -p 8000 -c-1
```

```
var http = require('http');

//create a server object:
http.createServer(function (req, res) {
  res.write('Hello World!'); //write a response to the client
  res.end(); //end the response
}).listen(8080); //the server object listens on port 8080
```

## Express

var express = require("express");

// Set up the express app
const app = express();
// get all todos
app.get('/api/v1/todos', (req, res) => {
  res.status(200).send({
    success: 'true',
    message: 'todos retrieved successfully',
  })
});
const PORT = 5002;

app.listen(PORT, () => {
  console.log(`server running on port ${PORT}`)
});

http://localhost:5002/api/v1/todos

## Install  node: https://jscomplete.com/learn/1rd-reactful

mkdir mydir; cd mydir

npm init
```
npm i express  
```
This command will download the express npm package and place it under a node_modules folder (which it will create because express is the first package to get installed). The command will also save this dependency to your package.json file.
```
npm install express --save
```
The save flag is used to edit your package.json file and add express as a dependency. After the installation is complete, open up your package.json to see express listed as a dependency. With this, you could send just your code and package.json file to a friend and request them to use npm to install the dependencies on their computer saving you some amount of data. To install, your friend will have to open up cmd inside the app folder and use the command npm install.

### Installing Development Dependencies

The following are dependencies that are not needed in production. To track them separately, you can use the npm -D install flag to save them under a devDependencies section in package.json.

When you run a Node server and then change the code of that server, you need to restart Node. This will be a frustrating thing in development. Luckily, there are some workarounds. The most popular one is Nodemon:

npm i -D nodemon

This package will make the nodemon command available in your project. Nodemon runs your Node server in a wrapper process that monitors the main process and automatically restarts it when files are saved to the disk. Simple and powerful!


A single TAB in Node’s REPL can be used for autocompletion

Double TAB (which is pressing the TAB key twice) can be used to see a list of possible things you can type from whatever partially-typed string you have.

Try:

Array.

Press TAB and see all the functions and properties that can be used from the Array class.

## Code
<https://medium.com/@maison.moa/create-a-simple-weather-app-using-node-js-express-and-react-54105094647a>
<https://www.smashingmagazine.com/2019/02/node-api-http-es6-javascript/>

## HTTP GET  <https://www.twilio.com/blog/2017/08/http-requests-in-node-js.html>
```
const https = require('https');

https.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY', (resp) => {
  let data = '';

  // A chunk of data has been recieved.
  resp.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received. Print out the result.
  resp.on('end', () => {
    console.log(data);
    //console.log(JSON.parse(data).explanation);
  });

}).on("error", (err) => {
  console.log("Error: " + err.message);
});

```

```
var http = require('http');
var URL="http://54.237.205.178:3010/api/v1/rooms/status"

var reqGet = http.get(URL, function(res) {
    console.log("Hii");
    console.log("\n statusCode: ", res.statusCode);

    res.on('data', function(d) {
        console.info('GET result:\n');
        process.stdout.write(d);
        console.info('\n\nCall completed');
    });

});

reqGet.end();
reqGet.on('error', function(e) {
    console.error("\n ERROR" +e);
});

```

<https://nodejs.org/api/events.html#events_events>

<http://expressjs.com/> ExpressJS

In terminal type: node
The NodeJS RELP will appear
Press tab twice to the list of all node modules

<https://github.com/nvm-sh/nvm> .  node version manager


<https://drive.google.com/file/d/1_CZCg0taMTNdWYznpxnTsPi5U9txZo3n/view> . Flavio Copes NodeJS handbook


<https://coffeencoding.com/cra-vs-next-js-vs-gatsby/>

### Create Reac App
Create React App is plain simple and it generates HTML code needed to render on the client side. So when you look at the source code before rendering, you can see it’s basically few js files and an empty div. 
These js files inject content into that div in the browser (Client-side rendering). All heavy lifting is done in the browser.

### Next.js 
Next.js a somewhat similar to Create React App, but supports server-side rendering. What it essentially means is that necessary HTML code is generated from the server itself, based on the URL. 
So your browser is receiving pre-rendered HTML code, not an empty ‘div’.

### Gatsby
Gatsby is something called “Static Site Generator”. 
It build “HTML” code during the “build”, by fetching data from some APIs, markdown files or anything.
Note that everything is done in the “build” process. 
Similar to Next.js browser receives pre-rendered HTML code.

## How to prerender React App on Server
<https://coffeencoding.com/prerender-react-app-for-seo-without-ssr-or-next-js/>
