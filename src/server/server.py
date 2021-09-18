import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World this is a python command executed from the backend")

# when you execute a python script, there is a main entry that gets executed first
if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler)
    ])

    port = 3000
    app.listen(port)
    print(f"Application is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()