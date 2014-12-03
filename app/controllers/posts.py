from ferris import Controller, route

class Posts(Controller):

    def list(self):
        return 'list'
    
    @route
    def test(self):
        return 'test'
    
    def run(self):
        return 'run'
