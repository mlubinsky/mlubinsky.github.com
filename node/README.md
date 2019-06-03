## Books
<https://jscomplete.com/learn/node-beyond-basics>
<<https://flaviocopes.com/> JS, Node, Express, React books>

<https://medium.com/@maison.moa/create-a-simple-weather-app-using-node-js-express-and-react-54105094647a>
<https://www.smashingmagazine.com/2019/02/node-api-http-es6-javascript/>


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
