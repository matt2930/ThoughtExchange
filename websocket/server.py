import socketio
from aiohttp import web

sio = socketio.AsyncServer(logger=True, engineio_logger=True, async_mode='aiohttp')
app = web.Application()
sio.attach(app)

@sio.event
def connect(sid, environ, auth):
    print('connect',sid)

@sio.event
def disconnect(sid):
    print('disconnect',sid)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8080)
