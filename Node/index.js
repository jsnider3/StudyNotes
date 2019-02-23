var server = require("./server.js");
var requestHandlers = require("./requestHandlers.js");
var router = require("./router.js");

var handle = {}
handle["/"] = requestHandlers.start;
handle["/start"] = requestHandlers.start;
handle["/upload"] = requestHandlers.upload;

server.start(router.route, handle);