class User():
    def __init__(self, name = ''):
        self.name = name

    def setName(self, name):
        if name:
            self.name = name

    def getName(self):
        return self.name