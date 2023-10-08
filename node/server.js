var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

var totalmembyt = os.totalmem();
var totalmemoryMB = totalmembyt / 1024 / 1024;

var freememorybytes = os.freemem()
var freememoryMB = freememorybytes / 1024 / 1024;

var uptimeInSeconds = os.uptime()
var days = Math.floor(uptimeInSeconds / (24 * 60 * 60));
var remainingSecAfterdays = uptimeInSeconds % (24 * 60 * 60);
var hours = Math.floor(remainingSecAfterdays / (60 * 60));
var remainingSecondsAfterHours = remainingSecAfterdays % (60 * 60);
var minutes = Math.floor(remainingSecondsAfterHours / (60));
var seconds = remainingSecondsAfterHours % 60;

var cpuinfo = os.cpus();
var numofCpu = cpuinfo.length;

http.createServer(function(req, res){

    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
}
    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        html=`    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: days: ${days},Hours: ${hours},Minutes: ${minutes},Seconds: ${seconds.toFixed(1)}</p>
            <p>Total Memory: ${totalmemoryMB.toFixed(3)} MB</p>
            <p>Free Memory: ${freememoryMB.toFixed(2)} MB</p>
            <p>Number of CPUs: ${numofCpu}</p>            
          </body>
        </html>` 
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000");

	