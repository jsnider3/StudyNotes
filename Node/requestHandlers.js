function start() {
  console.log("Request Handler Start was called.");
  return "Hello Start";
}

function upload() {
  console.log("Request Handler Upload was called.");
  return "Hello Upload";
}

exports.start = start;
exports.upload = upload;