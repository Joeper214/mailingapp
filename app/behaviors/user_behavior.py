from ferris.core.ndb import Behavior
from app.behaviors.sanitize import Sanitize


class UserBehavior(Behavior):
    sanitizer = Sanitize()
    
    def before_put(self, instance):
        instance.email = self.sanitizer.sanitize_email(instance.email)
        instance.password = self.sanitizer.sanitize_text(instance.password)

        
