// Lecture 10 - CSC 210 Fall 2015
// Philip Guo

// This example was adapted from http://socket.io/get-started/chat/
// (Comments added by Philip Guo)

// To run this example, first install Node.js on your computer, then
// run 'npm install' in this directory (maybe with 'sudo' if you need
// root permissions). Then run:
//
// node index.js
//
// to start the server and visit http://localhost:3000/ in your browser
// to see index.html being loaded.


// THIS CODE RUNS ON THE SERVER!

var app = require('express')(); // create a new Web app
var http = require('http').Server(app); // start an http server
var io = require('socket.io')(http); // create a socket.io object on the server


// If the user visits http://localhost:3000/ to request the '/' resource
// from localhost, then run the code below. This pattern matches using
// the first parameter string '/'. If this parameter were '/cat', then the
// relevant URL to trigger this function would be http://localhost:3000/cat
app.get('/', function(req, res){
  // load the index.html file and send it verbatim to the user's Web browser
  // (this is similar to the CGI script technique of 'printing' an HTML
  //  file to send its data to the user's browser)
  res.sendFile(__dirname + '/index.html');
});

// when a user's browser makes a socket.io (i.e., WebSocket) connection,
// run this outer function ... (note that this outer function runs *once* for
// every new user that connects to this server using 'var socket = io();' in
// index.html, as soon as they connect)
io.on('connection', function(socket){
  // when *any* user sends a 'chat message' to the server, run the inner
  // function below ...
  // (note that this inner function runs only when someone sends a message to
  // the server. if nobody is sending messages, this function never runs)
  socket.on('chat message', function(msg){
    // emit (send) the message msg verbatim to ALL BROWSERS
    // that are currently connected to the server at this moment
    io.emit('chat message', msg);
  });
});

// listen for connections on port 3000 so that browsers can connect by
// visiting this URL: http://localhost:3000/
http.listen(3000, function(){
  console.log('listening on *:3000');
});
