import web 

urls = (
	'/hello','index'
)

app = web.application(urls,globals())

render = web.template.render('C:/Users/Administrator/Desktop/learnpythonthehardway/projects/gothonweb/templates')

class index(object):
	def GET(self):
		# form = web.input(name = "Nobody")
		# greeting = "Hello %s! %s" % (form.name,form.greet)
		return render.hello_form()
		
	
	def POST(self):
		form = web.input(name= "Nobody",greet ="Hello")
		greeting = "%s, %s" % (form.greet,form.name)
		return render.index(greeting = greeting)
		
if __name__ == "__main__":
	app.run()
