from google.appengine.ext import ndb
from google.appengine.api import memcache
from app.models.mail import Mail

from app.models.mail import Mail

class Mails(object):

    def __init__(self, controller):
        self.controller = controller
        mail = Mail()

        
