const axios=require("axios")
const express=require("express")

//const PostgREST_URL="http://localhost:3000/"
const PostgREST_URL="http://54.237.205.178:3000/"

const URL_ROOMS_LIST="/api/v1/rooms"
const URL_ROOMS_STATUS="/api/v1/rooms/status"

const app = express();


const getData = async url => {
   try {
        const response = await axios.get(url)
        const data = response.data
        console.log(data)
        return data
       } catch (error) {
         console.log(error)
         return error
       }
}

app.get(URL_ROOMS_LIST, (req, res) => {
  const table="rooms";
  getData(PostgREST_URL + table)
    .then(function(result){
        console.log("result for "+table)
        console.log(result)
        obj={}
        obj["rooms"]=result
        console.log(obj)
        res.status(200).send(obj)
     })
});

app.get(URL_ROOMS_STATUS, (req, res) => {
  const table="last_measurement";
  getData(PostgREST_URL + table)
    .then(function(result){
        console.log("result for "+table)
        console.log(result)
        obj={}
        obj["rooms"]=result
        console.log(obj)
        res.status(200).send(obj)
     })
});


const PORT = 3011;

app.listen(PORT, () => {
  console.log(`server running on port ${PORT} localhost`)
  console.log(`localhost:${PORT}${URL_ROOMS_LIST}`)
  console.log(`localhost:${PORT}${URL_ROOMS_STATUS}`)
});
