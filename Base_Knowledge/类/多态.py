class Doc:
    def __init__(self, name):
        self.name = name

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Excel(Doc):
    def show(self):
        print('Excel')

class Word(Doc):
    def show(self):
        print('Word')


docs = [Excel('财务报表'), Word('企业文化')]

for d in docs:
    d.show()