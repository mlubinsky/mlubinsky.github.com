
const express = require("express");
const request = require("request");

// Set up the express app
const PostgREST_URL="http://localhost:3000/"
const URL_ROOMS_LIST="/api/v1/rooms"
const URL_ROOMS_STATUS="/api/v1/rooms/status"

// curl -- request http://localhost:3010/api/v1/rooms/status

async function get (url) {
  return new Promise((resolve, reject) => {
    request({ url, method: 'GET', json: true }, (error, response, body) => {
      if (error) return reject(error)

      return resolve({ body, response })
    })
  })
};


async function sendRequest (url) {
  let { response, body } = await get(url)

  if (response.statusCode !== 200) {
      return error(response, body)
  }

  return success(response, body)
}

function success (response, body) {
    console.log(`Status: ${response.statusCode}`)
    console.log(`Message: ${response.statusMessage}`)
    console.log(body)
    return body
}
function error (response) {
    console.log(`Status: ${response.statusCode}`)
    console.log(`Message: ${response.statusMessage}`)
    return response.statusCode
}


const app = express();

app.get(URL_ROOMS_LIST, (req, res) => {
  const table="rooms";
  sendRequest(PostgREST_URL + table)
    .then(function(result){
        console.log("result for "+table)
        obj={}
        obj["rooms"]=result
        console.log(obj)
	//r=JSON.parse(obj)
        res.status(200).send(obj)
     })
});

app.get(URL_ROOMS_STATUS, (req, res) => {
  const table="last_measurement";
  sendRequest(PostgREST_URL + table)
    .then(function(result){
        console.log("result for "+table)
        var obj={}
        obj["rooms"]=result
        console.log(obj)
	//r=JSON.parse(obj)
        res.status(200).send(obj)
     })
});

const PORT = 3011;

app.listen(PORT, () => {
  console.log(`server running on port ${PORT} localhost`)
  console.log(`localhost:${PORT}${URL_ROOMS_LIST}`)
  console.log(`localhost:${PORT}${URL_ROOMS_STATUS}`)
});
