const http = require("http");
const fs = require("fs");
const path = require("path");

const PORT = 5000;

http.createServer((req,res)=>{

    let filePath = "./index.html";

    if(req.url === "/style.css"){
        filePath = "./style.css";
    }

    if(req.url === "/script.js"){
        filePath = "./script.js";
    }

    const ext = path.extname(filePath);

    let contentType = "text/html";

    if(ext === ".css"){
        contentType = "text/css";
    }

    if(ext === ".js"){
        contentType = "text/javascript";
    }

    fs.readFile(filePath,(err,data)=>{
        if(err){
            res.writeHead(500);
            res.end("Server Error");
            return;
        }

        res.writeHead(200,{
            "Content-Type":contentType
        });

        res.end(data);
    });

}).listen(PORT,()=>{
    console.log(`Server running at http://localhost:${PORT}`);
});