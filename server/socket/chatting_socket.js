module.exports = function(server, Room)
{
    var io = require('socket.io')(server);
        console.log("[-] SOCKET FUNC IS RUNNING")

    var chat = io.of('/chat').on('connection', function(socket) {
        socket.on('get', function(data){
            console.log('message : ', data);
      
            var user = socket.user = data.user;
            var room = socket.room = data.room;
          
            var room = new Room({
                room_id: room,
                chatting_data: [{
                    seq: 1,
                    user_id: user,
                    chat: data.msg
                }]
            })

          socket.join(room);
      
          chat.to(room).emit('get', data.msg);
        });
    });
}