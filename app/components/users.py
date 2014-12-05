from google.appengine.ext import ndb
from app.models.user import User


class Users(object):

    
    def __init__(self, controller):
        self.controller = controller
        self.user = User()
        
    def authenticate(self):
        if self.controller.request.method == 'POST':
            email = self.controller.request.params['email']
            password = self.controller.request.params['password']
            u = self.user.find_by_email(email)
            print u
            if u is None:
                self.controller.context['email'] = email
                self.controller.context['msg'] = 'Invalid email or password'
            else:
                if u.password == password:
                    return self.controller.redirect(self.controller.uri(controller='mails', action='index', email=email))
                else:
                    self.controller.context['email'] = email
                    self.controller.context['msg'] = 'Invalid email or password'


    def signup(self):
        if self.controller.request.method == 'POST':
            email = self.controller.request.params['email']
            password = self.controller.request.params['password']
            confirm_pass = self.controller.request.params['confirm_pass']
            params = {'email': email, 'password': password}
            
            if password != confirm_pass:
                self.controller.context['e_msg'] = 'Password and Confirm Password does not match' 
            else:
                self.user.create(params)
                self.controller.context['s_msg'] = 'You registration successfully completed'
                

    
