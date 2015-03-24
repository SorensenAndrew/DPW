# Andrew Sorensen, DPW 03/15

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
    </head>'''
        page_body = '''
    <body>
        <form method="GET" action="">
        <label>Name: <input type="text" name="user"/>
        <label>Email: <input type="text" name="email"/>
        <button type="submit">Submit
        '''
        page_close = '''
        </form>
    </body>
</html>  '''

        if self.request.GET:
            user = self.request.GET['user']
            email = self.request.GET['email']
            self.response.write(page_head + user + ' ' + email + page_body + page_close)
        else:
            self.response.write(page_head + page_body + page_close)

        #self.response.write(page) #prints the arguments


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
