
kids = [
    {'name': 'xiaoming', 'score': 99, 'age': 12},
    {'name': 'xiaohong', 'score': 75, 'age': 13},
    {'name': 'xiaowang', 'score': 88, 'age': 15}
]

print(kids)

print(sorted(kids, key = lambda x: x['score']))


from operator import itemgetter

print(sorted(kids, key = itemgetter('score', 'age')))

from operator import attrgetter
class Kid:
    def __init__(self, name, score, age):
        self.name = name
        self.score = score
        self.age = age

    def __repr__(self):
        return 'Kid, name: {}, score: {}, age: {}'.format(self.name, self.score, self.age)

    def __lt__(self, other):
        return self.score > other.score or (self.score == other.score and self.age < other.age)

kids = [Kid('xiaoming', 99, 12), Kid('xiaohong', 99, 13), Kid('xiaowang', 88, 15), Kid('xiaoli', 99, 11)]

print(sorted(kids))
