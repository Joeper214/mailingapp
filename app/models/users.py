from ferris import BasicModel, ndb
from ferris.behaviors import searchable

class Users(BasicModel):
    class Meta:
        behaviors = (searchable.Searchable,)
        search_index = ('global',)

    email = ndb.StringProperty()
    password = ndb.StringProperty()

    @classmethod
    def list(cls):
        return cls.query().order(cls.email).fetch()

    @classmethod
    def create(cls, params):
        item = cls(email = params['email'],
                   password = params['password'])
        item.put()


    @classmethod
    def query_key(cls, keyname):
        instance = ndb.Key(cls, keyname).get()
        if instance is not None:
            return instance
        return None

    

        
