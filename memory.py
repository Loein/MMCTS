

class Mem:
    ''' gives a graph and returns the memorized value
    '''
    def __init__(self, length= 10, update_rate=0.2):
        self.length = length
        self.update_rate = update_rate
        self.keys = []
        self.items = {}

    def query(self, graph):
        for i, key in enumerate(self.keys):
            if key == graph:
                # item found
                self.keys.append(self.keys.pop(i)) # update sequence
                return self.items[key]
        # item not found
        # will not add item
        return 0

    def update(self, graph, value):
        for i, key in enumerate(self.keys):
            if key == graph:
                # item found
                self.keys.append(self.keys.pop(i)) # update sequence
                self.items[key] = self.update_rate * value + (1-self.update_rate) * self.items[key]
                return True
        # item ont found
        # add new item
        if len(self.keys) == self.length:
            self.items.pop(self.keys.pop(0))
        self.keys.append(graph)
        self.items[graph] = value
        return False
