// 귀여운 익스프레스 친구와 몽거위 새끼 대려옴
var express = require("express")
var mongo = require("mongoose")

// HOST & PORT
var HOST = '0.0.0.0'
var PORT = 5555

var server = express().listen(PORT, HOST, function(){
    console.log("Server has started on "+ HOST + ":" + PORT)
})