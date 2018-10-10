from . import session

class Discourse(object):
    
    def __init__(self,id):
        self.id = id

    def info(self):
        path = 'http://forum.mattermost.org/posts/{}'.format(self.id)
        response = session.get(path)
        return response.json()
