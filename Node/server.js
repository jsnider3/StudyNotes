var http = require("http");
var url = require("url");

function start(route, handle) {
  function onRequest(request, response) {
    var pathname = url.parse(request.url).pathname;
    console.log("Request for " + pathname + " received.");

    var content = route(handle, pathname);
    if (content) {
      response.writeHead(200, {"Content-Type": "text/plain"});
      response.write(content);
    }
    else {
      response.writeHead(404, {"Content-Type": "text/plain"});
    }
    response.end();
  }

  http.createServer(onRequest).listen(8888);

  console.log("Server running.");
}

exports.start = start;