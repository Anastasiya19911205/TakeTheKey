

class DataMixin:
	def get_user_context(self,**kwargs):
		context = kwargs
		return context

class Queue:
    FIFO = "FIFO"
    LIFO = "LIFO"
    STRATEGIES = [FIFO, LIFO]
    def __int__(self,strategy):
        if strategy not in self.STRATEGIES:
            raise ValueError(f'{strategy} not in supported strategies:{self.strategy}')

        self.storage = []
        self.strategy = strategy

    def add(self, value):
        if self.strategy == self.FIFO:
            self.storage.insert(0,value)
        elif self.strategy == self.LIFO:
            self.storage.append(value)
    def pop(self):
        return self.storage.pop()

