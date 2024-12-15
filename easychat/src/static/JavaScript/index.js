$(document).ready(function () {
    var socket = io()
    socket.on('connect', function () {
        socket.send('客户端已连接')
    });

    //前端发送消息给后端
    $('form#send_message').submit(function (event){
        socket.emit('send_message',{
            message:$('#message').val(),
        })
        return false
    });
    //加入房间
    $('form#join_room').submit(function (event){
        socket.emit('join_room',{
            room:$('#room_num').val(),
        })
        return false
    });
    //加入房间通知
    socket.on('room_joined', function (data) {
        $('#chat_content').append('<li>'+ data["username"]+"已加入房间"+data["room"] + '</li>');
    });

    //离开房间
    $('#leave_room_button').click(function (event){
        socket.emit('leave_room',{
            room:$('#room_num').val(),
        })
        return false
    });

    //离开房间其他人的通知
    socket.on('room_lefted', function (data) {
        $('#chat_content').append('<li>'+data["username"]+"已离开房间"+data["room"]+ '</li>')
    });
    //离开房间个人通知
    socket.on('room_lefted_personal', function (data) {
        $('#chat_content').append('<li>'+"您已离开房间"+data["room"]+ '</li>')
    });
    //发送消息到服务器
    $('form#submit_from').submit(function () {
        socket.emit("send_message",{
            message:$('#message').val(),
            room:$('#room_num').val(),
        });
        $('#message').val('');
        return false
    })
    //展示已发送的消息
    socket.on('sent_message', function (data) {
        $('#chat_content').append('<li>'+data["username"]+':'+data["message"] + '</li>')
    });


})
