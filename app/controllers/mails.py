from ferris import Controller, route
from google.appengine.api import memcache
from app.models.user import User
from app.models.mail import Mail

class Mails(Controller):
    mail = Mail()
    
    def list(self):
        return 'list'
    
    @route
    def index(self, email):
        data = memcache.get('mail_results')
        mail = []
        if data is None:
            source = 'From Datastore'
            data = self.mail.list()
            memcache.add('mail_results', data, 60)
        else:
            source = 'From Memcache'

        if self.request.method=='POST':
            subject = self.request.params['subject']
            for item in data:
                if item.subject == subject and item.recipient == email:
                    mail.append(item)
        else:
            for item in data:
                if item.recipient == email:
                    mail.append(item)
            

        self.session['user']    = email
        self.context['source']  = source
        self.context['email']   = email
        self.context['inboxes'] = mail

    @route
    def sentmails(self, email):
        data = memcache.get('mail_results')
        mail = []
        if data is None:
            source = 'From Datastore'
            data = self.mail.list()
            memcache.add('mail_results', data, 60)
        else:
            source = 'From Memcache'

        if self.request.method == 'POST':
            subject = self.request.params['subject']
            for item in data:
                if item.subject == subject and item.sender == email:
                    mail.append(item)

        else:
            for item in data:
                if item.sender == email:
                    mail.append(item)
                    
            
        self.session['user']    = email
        self.context['source']  = source
        self.context['email'] = self.session['user']
        self.context['sentmails'] = mail

    @route
    def compose(self, email):
        if self.request.method=='GET':
            self.context['email'] = email
            
        if self.request.method=='POST':
            sender = self.request.params['sender']
            recipient = self.request.params['recipient']
            subject = self.request.params['subject']
            message = self.request.params['message']
            params = {'sender'   : sender,
                      'recipient': recipient,
                      'subject'  : subject,
                      'message'  : message}
            
            self.mail.create(params)
            self.context['status'] = 'added'
            self.context['email'] = sender

    def run(self):
        return 'run'
