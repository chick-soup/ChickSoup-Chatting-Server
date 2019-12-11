module.exports = function(server, Room)
{
    var io = require('socket.io')(server)
    console.log("[-] SOCKET FUNC IS RUNNING")

    var chat = io.on('connection', function(socket) {
        console.log("[-] CONNECTED the socket")
        socket.on('get', function(data){
            console.log('message : ', data);
      
            var user = socket.user = data.user;
            var room = socket.room = data.room;
          
            var roomModel = new Room({
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