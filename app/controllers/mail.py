from ferris import Controller, route
from app.models.users import Users
from app.models.mail import Mail

class Mail(Controller):
    mail = Mail()
    
    def list(self):
        return 'list'
    
    @route
    def index(self, email):
        self.context['email'] = email
        self.context['inboxes'] = self.mail.inboxes(email)

    @route
    def sentmails(self, email):
        self.context['email'] = email
        self.context['sentmails'] = self.mail.sentmail(email)

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
