from ferris import BasicModel, ndb
from ferris.behaviors import searchable

class Mail(BasicModel):
    class Meta:
        behaviors = (searchable.Searchable,)
        search_index = ('global',)

    sender = ndb.StringProperty()
    recipient = ndb.StringProperty(required = True)
    subject = ndb.StringProperty(required = True)
    message = ndb.TextProperty(required = True)

    @classmethod
    def list(cls):
        return cls.query().order(cls.created).fetch()

    @classmethod
    def inboxes(cls, email):
        return cls.find_all_by_recipient(email)

    @classmethod
    def sentmail(cls, email):
        return cls.find_all_by_sender(email)
    
    @classmethod
    def create(cls, params):
        item = cls(sender = params['sender'],
                   recipient = params['recipient'],
                   subject  = params['subject'],
                   message = params['message'])
        item.put()
        

    @classmethod
    def query_key(cls, keyname):
        instance = ndb.Key(cls, keyname).get()
        if instance is not None:
            return instance
        return None

        
