module.exports = function(server)
{
    var io = require('socket.io')(server);
    console.log("[-] SOCKET FUNC IS RUNNING")

    var chat = io.of('/chat').on('connection', function(socket) {
        socket.on('chat message', function(data){
          console.log('message from client: ', data);
      
          var name = socket.name = data.name;
          var room = socket.room = data.room;
      
          socket.join(room);
      
          chat.to(room).emit('chat message', data.msg);
        });
      });
}