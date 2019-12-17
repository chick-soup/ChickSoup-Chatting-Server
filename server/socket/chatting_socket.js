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
                _id: room,
                chatting_data: [{
                    user_id: user,
                    chat: data.msg
                }]
            })

            roomModel.save()

            socket.join(room);
      
            socket.broadcast.to(room).emit('get', data.msg);
        });
    });
}