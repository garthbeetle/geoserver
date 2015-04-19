import webapp2
import json


#function that gets called from api/ takes query as argument.
def get_from_db(query):
	return {"rob": 1}


#set up webapp2 server. remember to cancel build often, or kill it in task manager
#app.yaml to configure.

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, weddadasdfadfbapp2!')


class APIHandler(webapp2.RequestHandler):
    def get(self, query):
    	data = get_from_db(query)
    	self.response.write(json.dumps(data))


app = webapp2.WSGIApplication([
    webapp2.Route('/api/<query>', APIHandler),
    webapp2.Route('/', HelloWebapp2),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()