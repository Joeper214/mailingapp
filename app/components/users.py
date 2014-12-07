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
                    return self.controller.redirect(self.controller.uri(controller='mails', action='index', user_email=email))
                else:
                    self.controller.context['email'] = email
                    self.controller.context['msg'] = 'Invalid email or password'


    def signup(self):
        if self.controller.request.method == 'POST':
            if self.is_valid_email():
                email = self.controller.request.params['email']
                password = self.controller.request.params['password']
                confirm_pass = self.controller.request.params['confirm_pass']
                params = {'email': email, 'password': password}
            
                if password != confirm_pass:
                    self.controller.context['email'] = email
                    self.controller.context['e_msg'] = 'Password and Confirm Password does not match' 
                else:
                    self.user.create(params)
                    self.controller.context['s_msg'] = 'You registration successfully completed'
            else:
                self.controller.context['e_msg'] = 'Please Input a Valid Email'


    def is_valid_email(self):
        email = self.controller.request.params['email']

        at_count = email.count('@')
        at_index = email.find('@')
        dot_count = email.count('.')
        dot_index = email.find('.')
        if len(email) <= 1:
            return False
        elif at_count == 0:
            return False
        elif at_index <= 0 or at_index==len(email)-1:
            return False
        elif dot_count == 0:
            return False
        elif dot_index <= 0 or dot_index == len(email)-1:
            return False
        elif at_index-dot_index == 1 or at_index-dot_index == -1:
            return False
        else:
            return True
