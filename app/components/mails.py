from google.appengine.ext import ndb
from google.appengine.api import memcache
from app.models.mail import Mail

from app.models.mail import Mail

class Mails(object):

    def __init__(self, controller):
        self.controller = controller
        mail = Mail()

    def index(self):
        data = memcache.get('mail_results')
        mail = []
        if data is None:
            source = 'From Datastore'
            data = self.mail.list()
            memcache.add('mail_results', data, 60)
        else:
            source = 'From Memcache'

        if self.controller.request.method=='POST':
            subject = self.controller.request.params['subject']
            for item in data:
                if item.subject == subject and item.recipient == email:
                    mail.append(item)
        else:
            for item in data:
                if item.recipient == email:
                    mail.append(item)
            

        self.controller.session['user']    = email
        self.controller.context['source']  = source
        self.controller.context['email']   = email
        self.controller.context['inboxes'] = mail


    
