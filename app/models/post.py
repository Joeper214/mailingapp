from ferris import BasicModel, ndb
from ferris.behaviors import searchable

class Post(BasicModel):
    class Meta:
        behaviors = (searchable.Searchable,)
        search_index = ('global',)

    title = ndb.StringProperty()
    content = ndb.TextProperty()
    ratings = ndb.IntegerProperty()

    @classmethod
    def select_all(cls):
        return cls.query().order(cls.title).fetch()
