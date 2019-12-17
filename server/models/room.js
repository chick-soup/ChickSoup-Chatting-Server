let mongoose = require('mongoose')
let Schema = mongoose.Schema

let RoomModel = new Schema({
    _id: { type: String, unique: true },
    people: String,
    chatting_data: [{
        _id: false,
        user_id: String,
        chat: String
    }]
})

module.exports = mongoose.model('room', RoomModel)