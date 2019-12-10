// 귀여운 익스프레스 친구와 몽거위 새끼 대려옴
var express = require("express")
var server = require('http').createServer(express);
var mongo = require("mongoose")

// HOST & PORT
var HOST = '0.0.0.0'
var PORT = 5555

var db = mongo.connection
db.on('error', console.error)
db.once('open', function(){
    console.log("[-] Connected to mongo serv")
})

mongo.connect("mongodb://localhost/js_mongodb")

RoomModel = require('./models/room')

var socket = require('./socket/chatting_socket')(server, RoomModel)

server.listen(PORT, HOST, function(){
    console.log("Server has started on "+ HOST + ":" + PORT)
})