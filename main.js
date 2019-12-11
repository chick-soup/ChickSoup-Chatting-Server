var app = require('express')();
var server = require('http').createServer(app);
var io = require('socket.io')(server);


var chat = io.of('/chat').on('connection', function(socket) {
  console.log("chatter")
  socket.on('chat message', function(data){
    console.log('message from client: ', data);

    var name = socket.name = data.name;
    var room = socket.room = data.room;

    socket.join(room);

    chat.to(room).emit('chat message', data.msg);
  });
});

server.listen(3000, '0.0.0.0',function() {
  console.log('[-] 0.0.0.0 | 3000');
});