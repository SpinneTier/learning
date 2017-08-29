import tornado.ioloop
import tornado.web
import json
from bson import ObjectId
from pymongo import MongoClient
'''
1. главная страница - список тредов - MainHandler - GET - /
2. добавление треда - MainHandler - POST - /
3. список постов в треде - ThreadHandler - GET - /thread?id=THREAD_ID
4. добавление поста в тред - ThreadHandler - POST - /thread?id=THREAD_ID
[{"name": "мемы", "колво постов","posts": [
            {"author": "Аноним", "text": "текст поста"}]},
 {"name": "мемы", "колво постов", "posts": [
            {"author": "Аноним", "text": "текст поста"}]}]
'''
# создать конекшн к монге
connection = MongoClient("mongodb://User:Lil45Sev@ds013619.mlab.com:13619/gotoch")
# выбрать бд
database = connection['gotoch']
# выбрать коллекцию
threads_collection = database['threads']
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        threads = list(threads_collection.find())
        self.render("threads.htm", threads=threads)
    def post(self):
        name = self.get_argument('name')
        thread = {"name": name, "posts": []} 
        threads_collection.insert(thread)
        self.redirect('/')
class DelHandler(tornado.web.RequestHandler):
    def get(self):
      threads={threads_collection.find()}
      thread=threads_collection.find_one({'_id': ObjectId(self.get_argument('id'))})
      threads_collection.remove(thread,threads)
      self.redirect('/')
class ThreadHandler(tornado.web.RequestHandler):
    def get(self):
        thread=threads_collection.find_one({'_id': ObjectId(self.get_argument('id'))})
        self.render("posts.htm",thread=thread)
    def post(self):
        # добавление поста
        nik = self.get_argument("nik")
        post = self.get_argument("post")
        post = {"nik":nik, "post":post}
        threads_collection.insert(thread)
        # TODO: Получить параметры из запроса (self.get_argument...)
        # TODO: сделать новый пост
        # TODO: добавить пост в тред и сохранить в монге
        # TODO: редирект на страницу с постами
        self.redirect('/thread')
class KomHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("koms.htm", name="name", post="post", nik="nik")
    def post(self):
        nik = self.get_argument("nik")
        kom = self.get_argument("kom")
        kom = {"nik":nik, "kom":post, "qkom":qkom}
        threads_collection.insert(thread)
        self.redirect('/koms')
routes = [
    (r"/", MainHandler),
    (r"/delete", DelHandler),
    (r"/thread", ThreadHandler),
    (r"/koms", KomHandler)
]
app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()
