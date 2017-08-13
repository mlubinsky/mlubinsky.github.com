console.log("Hello");
console.log(module);

const fs=require('fs');
const os=require('os');

const notes=require("./myfile.js");
console.log(notes.age);
var res = notes.addNote();
console.log(res);
console.log(notes.add(2,3));
console.log(process.argv);

//var user=os.userInfo();
//fs.appendFile("myfile.txt","HellowWorld #1" +user.username);
//fs.appendFile("myfile.txt",`HellowWorld  ${user.username}`);
//fs.appendFileSync("myfile.txt","HellowWorld #2");

