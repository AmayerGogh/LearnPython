class Query(object):
    
    def __enter__(self):
        print('begin')
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        if exc_type:
            print('error')
        else:
            print('end')
    def query(self):
        print('query info about %s' % self.name)
    def __init__(self,name):
        self.name =name
        print('init')
with Query('boob') as q:
    q.query()