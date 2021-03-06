from ferris import Controller, messages, route
from google.appengine.api import memcache
from app.models.mail import Mail
from app.components.mails import Mails


class Mails(Controller):

    class Meta:
        prefixes = ('api',)
        components = (Mails, messages.Messaging)
        Model = Mail

    @route
    def index(self, user_email):
        self.components.mails.inbox(user_email)

    @route
    def sentmails(self):
        self.components.mails.sentmails()

    @route
    def compose(self):
        self.components.mails.compose_mail()

    @route
    def index2(self, user_email):
        self.components.mails.inbox(user_email)

    @route
    def api_test(self):
        self.context['data'] = Mail.find_all_by_recipient('Joeper.Serrano@gmail.com')

    @route
    def api_compose(self):
        post = self.request.POST()


        Mail.compose(post)

        mail = Mail()
        mail.recipient = post.get('recipient')
        mail.put()
