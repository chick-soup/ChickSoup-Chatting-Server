let mongoose = require('mongoose')
let Schema = mongoose.Schema

let RoomModel = new Schema({
    room_id: { type: String, unique: true},
    people: String,
    chatting_data: [{
        seq: Number,
        user_id: String,
        chat: String
    }]
})

module.exports = mongoose.model('room', RoomModel)