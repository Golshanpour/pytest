class Queue(object):
    """
    Queue init
    """
    def __init__(self, lenth):
        """
        lenth parameter explain lenth of queue by user order
        """
        self.queue = []
        self.front = None
        self.rear = None
        self.lenth = lenth
        self.size = 0

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def size(self):
        """
        returns the current size of the queue
        """
        return self.size

    def is_empty(self):
        """
        checks if the queue is empty
        """
        return self.size <= 0

    def enqueue(self, data):
        """
        inserts an item into the queue
        """
        if self.size >= self.lenth:
            # queue overflow
            return -1
        else:
            self.queue.append(data)

        # assign the rear as size of the queue and front as 0
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size

        self.size += 1

    def dequeue(self):
        """
        pops an item from the queue which was first inserted
        """
        if self.is_empty():
            # queue underflow
            return None
        else:
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = 0
            else:
                self.rear = self.size - 1
            return self.queue.pop(0)

#=================================================
#================ for example ====================
  
import random
q1 = Queue(10)
for i in range(10):
    r_ = random.randint(101, 999)
    q1.enqueue(r_)

print('my queue dictionary is : ',q1.__dict__)
print('size :',q1.size)
print('front :',q1.front)
print('rear :',q1.rear)
print(type(q1), 'queue is =====>> ', q1)
print('pop item :',q1.dequeue())
print('items remained in queue =====>> ',q1)
