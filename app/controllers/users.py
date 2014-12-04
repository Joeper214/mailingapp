from ferris import Controller, route
from app.models.users import Users

class Users(Controller):
    u = Users()
    
    def list(self):
        return 'list'
    
    @route
    def login(self):

        if self.request.method == 'POST':
            email = self.request.params['email']
            password = self.request.params['password']
            user = self.u.find_by_email(email)
            if None:
                self.context['msg'] = 'Invalid email or password' 
            else:
                if user.password == password:
                    return self.redirect(self.uri(controller='mail', action='index', email=email))
                else:
                    self.context['msg'] = 'Invalid email or password'

    @route
    def signup(self):
        if self.request.method == 'POST':
            email = self.request.params['email']
            password = self.request.params['password']
            confirm_pass = self.request.params['confirm_pass']
            params = {'email': email, 'password': password}

            if password != confirm_pass:
                self.context['e_msg'] = 'Password and Confirm Password does not match' 
            else:
                self.u.create(params)
                self.context['s_msg'] = 'You registration successfully completed'



                

    def run(self):
        return 'run'
