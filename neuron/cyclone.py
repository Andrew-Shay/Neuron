# -*- coding: utf-8 -*-
# Starts Tornado which runs Flask

from tornado.ioloop import IOLoop
from tornado.web import FallbackHandler, RequestHandler, Application
from tornado.wsgi import WSGIContainer

from neuron.app import app


class MainHandler(RequestHandler):
    def get(self):
        self.write("Tornado")


tr = WSGIContainer(app)
application = Application([
    (r"/tornado", MainHandler),
    (r".*", FallbackHandler, dict(fallback=tr)),
])


def start_cyclone(app_port):
    """
    Starts tornado to run Flask
    :param int app_port: Port for the server to use
    """
    try:
        application.listen(app_port)
        print("Tornado Started:" + str(app_port))
        IOLoop.instance().start()
    except:
        print("Failed to start Tornado")


if __name__ == "__main__":
    start_cyclone(5000)
