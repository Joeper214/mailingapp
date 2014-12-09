import re

class Sanitize(object):
    
    def __init__(self):
        self.invalidemailtags = ['<', '\/', '>', '\\', '?', '\'', '(', ')', ',', ';']
        self.invalidtags = ['<', '\/', '>', '\\', '\'']

    def sanitize_email(self, text):
        clean_text = re.sub('[%s]' % ''.join(self.invalidemailtags), '', text)
        return clean_text

    def sanitize_text(self, text):
        clean_text = re.sub('[%s]' % ''.join(self.invalidtags), '', text)
        return clean_text
        
        

