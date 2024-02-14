class User():
    def __init__(self, name = ''):
        self.name = name
        print('init user')

    def id(self):
        print('id')

    def setName(self, name):
        if name:
            self.name = name

    def getName(self):
        return self.name

    def quizes_taken(self):
        print('quizes taken')