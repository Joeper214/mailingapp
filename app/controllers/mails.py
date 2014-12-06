from ferris import Controller, route
from google.appengine.api import memcache
from app.models.mail import Mail
from app.components.mails import Mails

class Mails(Controller):

    class Meta:
        components = (Mails,)
        

    @route
    def index(self, user_email):
        self.components.mails.inbox(user_email)

    @route
    def sentmails(self):
        self.components.mails.sentmails()

    @route
    def compose(self):
        self.components.mails.compose_mail()
