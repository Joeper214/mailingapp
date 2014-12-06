from ferris import Controller, route
from google.appengine.api import memcache
from google.appengine.ext import ndb
from app.models.user import User
from app.components.users import Users

class Users(Controller):

    class Meta:
        components = (Users,)
        model = User
        
    @route
    def login(self):
        return self.components.users.authenticate()
    

    @route
    def signup(self):
        self.components.users.signup()
