import tornado.ioloop
import tornado.web
import images
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<center><h2>Привет. У меня есть к тебе вопрос... Или два...</h2></center>")
        self.write("<center><form action='/ask'><button>Отвечу</button></form></center>")
        self.write('<center><img src="static/que.jpg"></center>')
# localhost:8888/discusion
class AskHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('n.htm')
class ChoiceHandler(tornado.web.RequestHandler):
    def get(self):
       color=self.get_argument("color")
       food=self.get_argument("food")
       place=self.get_argument("place") 
       self.render('disc.htm', color=color, food=food, place=place)
routes = [
    (r"/", MainHandler),
    (r"/ask", AskHandler),
    (r"/disc",ChoiceHandler),
    (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static'})]
app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()
