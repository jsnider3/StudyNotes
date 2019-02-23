var formidable = require("formidable");
var fs = require("fs");
var querystring = require("querystring");

function start(response) {
  console.log("Request Handler Start was called.");
  var body = '<html>' +
    '<head>' +
    '<meta http-equiv="Content-Type" content="text/html; ' +
    'charset=UTF-8" />' +
    '</head>' +
    '<body>' +
    '<form action="/upload" enctype="multipart/form-data" method="post">' +
    '<input type="file" name="upload" multiple="multiple">' +
    '<input type="submit" value="Upload file" />' +
    '</form>' +
    '</body>' +
    '</html>';
    response.writeHead(200, {"Content-Type": "text/html"});
    response.write(body);
    response.end();
}

function upload(response, request) {
  console.log("Request Handler Upload was called.");
  
  var form = new formidable.IncomingForm();
  console.log("about to parse");
  form.parse(request, function(error, fields, files) {
    console.log("parsing done");
    fs.rename(files.upload.path, "/Users/josh/Downloads/NewFile.png", function(error) {
      if (error) {
        fs.unlink("/Users/josh/Downloads/NewFile.png");
        fs.rename(files.upload.path, "/Users/josh/Downloads/NewFile.png");
      }
    });
    response.writeHead(200, {"Content-Type": "text/html"});
    response.write("received image: <br/>");
    response.write("<img src='/show' />");
    response.end();
  });
}

function show(response) {
  console.log("Request handler 'show' was called.");
  response.writeHead(200, {"Content-Type": "image/png"});
  fs.createReadStream("/Users/josh/Downloads/NewFile.png").pipe(response);
}

exports.start = start;
exports.upload = upload;
exports.show = show;