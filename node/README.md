<https://gregberge.com/blog/javascript-stack-2020>

https://nodemon.io/  utility that will monitor for any changes in your source and automatically restart your server. 

## Books
<https://jscomplete.com/learn/node-beyond-basics>

<https://habr.com/company/ruvds/blog/428576/> . PDF book

https://books.goalkicker.com/NodeJSBook/

<https://flaviocopes.com/> JS, Node, Express, React books 

<https://github.com/goldbergyoni/nodebestpractices> . Best Practices

<https://blog.logrocket.com/a-complete-guide-to-the-node-js-event-loop/> 

<https://blog.logrocket.com/handling-and-dispatching-events-with-node-js/> 



## Official Doc

<https://nodejs.org/api/>

## 101

<https://101node.io/>

<https://habr.com/ru/post/460661/>

<https://habr.com/ru/company/ruvds/blog/422893/> 

<https://habr.com/ru/post/435970/>

<https://habr.com/ru/company/ruvds/blog/341646/>

<https://habr.com/ru/post/434962/> . You do not need Express for REST API

<https://dzone.com/articles/node-cluster>

<https://habr.com/ru/company/funcorp/blog/461881/> logging in Node

## Input Validation

<https://hapijs.com/tutorials/validation>

<https://habr.com/ru/post/462189/>

## NodeJS in Docker

<https://habr.com/ru/company/ruvds/blog/454522/>

<https://habr.com/ru/company/ruvds/blog/440656/>

## GraphQL

<https://blog.bitsrc.io/migrating-existing-rest-apis-to-graphql-2c5de3db647d>

##  NestJS vs Next.js
Next.js предназначен, прежде всего, для серверного рендеринга, и привязан к React. 

<https://www.youtube.com/watch?v=iEUw_SNou7o>
NestJS — для разработки бэкенда, с которым фронтенд общается через GraphQL или REST, 
и ему все равно, как реализован фронтенд.

<https://habr.com/ru/post/439434/>

## HTPP Server
```
ls node_modules/http-server/
ls node_modules/.bin/
./node_modules/.bin/http-server -a localhost -p 8000 -c-1
```

## HTPP Server 2
```
const http = require('http')
const hostname = '127.0.0.1'
const port = 3000
const server = http.createServer((req, res) => {
  res.statusCode = 200
  res.setHeader('Content-Type', 'text/plain')
  res.end('Hello World\n')
})
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`)
})
```

## Express

<https://github.com/cdimascio/generator-express-no-stress>

<https://expressjs.com/en/guide/using-middleware.html>

```
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
```
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
```
Array.
```
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

### NodeJS + Oracle

<https://habr.com/ru/post/473234/>

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


## Links


<https://habrahabr.ru/post/133363/>
<https://www.twilio.com/blog/2017/08/working-with-environment-variables-in-node-js.html>
<https://www.twilio.com/blog/2017/08/http-requests-in-node-js.html>
```
https://nodehandbook.com/
https://github.com/i0natan/nodebestpractices
https://nodejs.org/en/docs/guides/
nodejs.org/api/

https://habr.com/post/430972/

https://habr.com/company/ruvds/blog/425667/  several articles
https://blog.bloomca.me/2018/06/21/nodejs-guide-for-frontend-developers.html
https://metanit.com/web/nodejs/
https://habrahabr.ru/company/ruvds/blog/322388/
https://habrahabr.ru/company/jugru/blog/341070/
https://habrahabr.ru/post/339870/
https://habrahabr.ru/post/278017/
https://habrahabr.ru/post/259987/
https://blog.sessionstack.com/
https://medium.com/the-node-js-collection/what-you-should-know-to-really-understand-the-node-js-event-loop-and-its-metrics-c4907b19da4c

https://medium.com/devschacht/node-hero-chapter-3-cae7333c7f3d
```



```
node --version
node
     >global      (like window in Chrome)
     >process     (like document in Chrome)
     >console.log(process.env);




var addNote=() => {title, body};
var removeNote=() => {title};
module.exports={ addNote : addNote, removeNote: removeNote};  - the same as next line
module.exports={ addNote, removeNote};


NVM (node version manager) to install any version you want and switch between them. You can use it to uninstall versions too.
https://github.com/creationix/nvm
nvm install 8.3.0
nvm use x.x.x

```

## NPM 
```
brew install node
npm list -g
ls -la /usr/local/lib/node_modules/npm

ls /usr/local/lib/node_modules/npm/node_modules/

JSONStream			detect-newline			lazy-property			mkdirp				pacote				sorted-object
abbrev				dezalgo				libcipm				move-concurrently		path-is-inside			sorted-union-stream
ansi-regex			editor				libnpmhook			node-gyp			promise-inflight		ssri
ansicolors			figgy-pudding			libnpx				nopt				qrcode-terminal			strip-ansi
ansistyles			find-npm-prefix			lock-verify			normalize-package-data		query-string			tar
aproba				fs-vacuum			lockfile			npm-audit-report		qw				text-table
archy				fs-write-stream-atomic		lodash._baseindexof		npm-cache-filename		read				tiny-relative-date
bin-links			gentle-fs			lodash._baseuniq		npm-install-checks		read-cmd-shim			uid-number
bluebird			glob				lodash._bindcallback		npm-lifecycle			read-installed			umask
byte-size			graceful-fs			lodash._cacheindexof		npm-package-arg			read-package-json		unique-filename
cacache				has-unicode			lodash._createcache		npm-packlist			read-package-tree		unpipe
call-limit			hosted-git-info			lodash._getnative		npm-pick-manifest		readable-stream			update-notifier
chownr				iferr				lodash.clonedeep		npm-profile			readdir-scoped-modules		uuid
cli-columns			imurmurhash			lodash.restparam		npm-registry-client		request				validate-npm-package-license
cli-table2			inflight			lodash.union			npm-registry-fetch		retry				validate-npm-package-name
cmd-shim			inherits			lodash.uniq			npm-user-validate		rimraf				which
columnify			ini				lodash.without			npmlog				safe-buffer			worker-farm
config-chain			init-package-json		lru-cache			once				semver				wrappy
debuglog			is-cidr				meant				opener				sha				write-file-atomic
detect-indent			json-parse-better-errors	mississippi			osenv				slide

npmjs.com
node -v
npm --version
npm init

npm install yargs@4.7.1   -- command line parser
npm install lodash --save   //will a) put package in ./node_modules/ and b) add  it in package.json (this is because of --save)
const _  = require ('lodash')

npm install nodemon -g
nodemon app.js   //will run node app.js every tyme when it updates

./node_modules/.bin/webpack --watch

npm install eslint -g
eslint --init      // from project directory http://fullstackhumanoid.com/quick-eslint-set-up-with-google-airbnb-or-standard-rulesets/
```
