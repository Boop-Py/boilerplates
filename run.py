import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    
    def post(self):
        print("posted ")
        json_input_data = self.get_argument("input")
        
        self.render("index.html", data = json_input_data)
        
    def get(self):
        data = ""
        self.render("index.html", data = data)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    print("Running on port 8888")
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()