from google.appengine.ext import ndb
from google.appengine.api import memcache
from app.models.mail import Mail


class Mails(object):

    def __init__(self, controller):
        self.controller = controller
        self.mail = Mail()

    def inbox(self, user_email):
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
                if item.subject == subject and item.recipient == user_email:
                    mail.append(item)
        else:
            for item in data:
                if item.recipient == user_email:
                    mail.append(item)
            

        self.controller.session['user_email'] = user_email
        self.controller.context['user_email'] = user_email
        self.controller.context['source']  = source
        self.controller.context['inboxes'] = mail

    def sentmails(self):
        user_email = self.controller.session['user_email']
        data = memcache.get('mail_results')
        mail = []
        if data is None:
            source = 'From Datastore'
            data = self.mail.list()
            memcache.add('mail_results', data, 60)
        else:
            source = 'From Memcache'

        if self.controller.request.method == 'POST':
            subject = self.controller.request.params['subject']
            for item in data:
                if item.subject == subject and item.sender == user_email:
                    mail.append(item)

        else:
            for item in data:
                if item.sender == user_email:
                    mail.append(item)
                    
            
        self.controller.session['user_email']    = user_email
        self.controller.context['user_email']    = user_email
        self.controller.context['source']  = source
        self.controller.context['sentmails'] = mail


    def compose_mail(self):
        if self.controller.request.method=='GET':
            self.controller.context['user_email'] = self.controller.session['user_email']
            
        if self.controller.request.method=='POST':
            sender = self.controller.session['user_email']
            recipient = self.controller.request.params['recipient']
            subject = self.controller.request.params['subject']
            message = self.controller.request.params['message']
            params = {'sender'   : sender,
                      'recipient': recipient,
                      'subject'  : subject,
                      'message'  : message}

            if self.is_valid_recipient():
                self.mail.create(params)
                self.controller.context['status'] = 'added'
                self.controller.context['user_email'] = sender
            else:
                self.controller.context['user_email'] = sender
                self.controller.context['subject'] = subject
                self.controller.context['message'] = message
                self.controller.context['e_msg'] = 'Please Input A valid and registered Recipient Email'



    def is_valid_recipient(self):
        recipient = self.controller.request.params['recipient']
        m = self.mail.find_by_recipient(recipient)
        if m is None:
            return False
        else:
            return True
