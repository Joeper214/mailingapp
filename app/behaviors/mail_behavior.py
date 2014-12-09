from ferris.core.ndb import Behavior
from app.behaviors.sanitize import Sanitize


class MailBehavior(Behavior):
    sanitizer = Sanitize()
    
    def before_put(self, instance):
        instance.sender = self.sanitizer.sanitize_email(instance.sender)
        instance.recipient = self.sanitizer.sanitize_email(instance.recipient)
        instance.subject = self.sanitizer.sanitize_text(instance.subject)
        instance.message = self.sanitizer.sanitize_text(instance.message)
