var http = require("http"); 
var data = require("C:/Users/SUBRA/Downloads/widgets.json")
var server = http.createServer(function(req, res){ 

    if (req.url === "/") { 

        res.writeHead(200, {"Content-Type": "text/json"}); 

        res.end(JSON.stringify(data)); 

    } 

    else if (req.url === "/blue") { 

        listBlue(res); 

    } else { 

        res.writeHead(404, {"Content-Type": "text/plain"});       

        res.end("Data not found");         

    } 

}); 

function listBlue(res) { 
    var colorBlue = data.filter(function(item) { 
        return item.color === "blue"; 
    }); 

    res.end(JSON.stringify(colorBlue)); 
}  