from flask import session
from flask_socketio import emit,join_room, leave_room
from .define_socket import my_socketio

print("导入文件")

@my_socketio.on('connect', namespace='/chat')
def connect():
    print("连接成功")


@my_socketio.on('join', namespace='/chat')
def join_room(information):
    # 'joined'路由是传入一个room_name,给该websocket连接分配房间,返回一个'status'路由
    room_name = information.get('client_to_server')
    username = session.get('username')
    join_room(room_name)
    emit('status', {'server_to_client': username +'has entered the room'}, room=room_name)


@my_socketio.on('left', namespace='/chat')
def left(information):
    room_name = information.get('client_to_server')
    username = session.get('username')
    leave_room(room_name)
    emit('status', {'server_to_client': username + ' has left the room'}, room=room_name)

@my_socketio.on('disconnect', namespace='/chat')
def disconnect():
    print("断开连接")

@my_socketio.on('message', namespace='/chat')
def message(information):
    room_name = information.get('client_to_server')
    username = session.get('username')
    emit('message', {'server_to_client': username +':'+information.get('message')}, room=room_name)




