class Sleigh(object):
    def authenticate(self, name, password):
        return name == 'Santa Claus' and password == 'Ho Ho Ho!'
        
 

class Sleigh(object):
    def authenticate(self, x, y):
        if (x,y) == ('Santa Claus','Ho Ho Ho!'):
            return True
        return False