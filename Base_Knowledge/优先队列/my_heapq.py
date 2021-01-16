import heapq

nums = [14, 9, 3, 47, 19, 25, 6, 1, 24, 33, 11]
print(heapq.nlargest(3, nums))

print(heapq.nsmallest(3, nums))



laptops = [
    {'name': 'ThinkPad', 'amount': 100, 'price': 91.1},
    {'name': 'Mac', 'amount': 50, 'price': 543.22},
    {'name': 'Surface', 'amount': 200, 'price': 21.09},
    {'name': 'Alienware', 'amount': 35, 'price': 31.75},
    {'name': 'Lenovo', 'amount': 45, 'price': 16.35},
    {'name': 'Huawei', 'amount': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, laptops, key=lambda dic: dic['price'])

print(cheap)

class PriorityQueue:

    def __init__(self):
        self._queue = []    #优先队列
        self._index = 0     #记录元素压栈顺序

    def push(self, name, priority):
        # 传入两个参数，一个是存放元素的数组，另一个是要存储的元素，这里是一个元组。
        # 由于heap内部默认由小到大排，所以对priority取负数
        heapq.heappush(self._queue, (-priority, self._index, name))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def print_queue(self):
        print(self._queue)


q = PriorityQueue()

q.push('lenovo', 1)
q.push('Mac', 5)
q.push('ThinkPad', 2)
q.push('Surface', 3)

q.print_queue()

print(q.pop())
# Mac
print(q.pop())
# Surface



