# -*- coding: utf-8 -*-
from cats import Cats, BaseSocketIO, render_template
import argparse

app = Cats()


class ViewTest:
    def get(self, request):
        return render_template('index.jinja', \
            {
             'host': args.host,
             'port': args.port
            }, request=request)

    def post(self, request):
        return 'you sent message: %s' % request.POST.get('post-msg')


class ViewTestSocketIO(BaseSocketIO):
    def on_todo(self, todo):
        self.emit('todo', todo)
        print(todo)

    def recv_disconnect(self):
        self.disconnect(silent=True)


# defining route
urls = [
        (r'^$', ViewTest),
        (r'^test2/.*$', ViewTest),
       ]
socketio_urls = [
        ('', ViewTestSocketIO),
       ]

app.routes(urls)
app.socketio_routes(socketio_urls)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Echo Gevent Server')
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('-p', '--port', default=9000, type=int)
    args = parser.parse_args()

    server = app.run(args.host, args.port)
    server.serve_forever()


