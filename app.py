from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class IndexPage(webapp.RequestHandler):
	def get(self):
		pass

app = webapp.WSGIApplication([('/.*', IndexPage)], debug=True)

def main():
	run_wsgi_app(app)

if __name__ == '__main__':
	main()