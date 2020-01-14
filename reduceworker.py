import itertools

class ReduceWorker:
    def __init__(self, reduceFunc, customKey=None):
        self.reduceFunc = reduceFunc
        self.sortKey = customKey
        self.intermediatePairs = []
        self.output = {}
    def receiveInput(self, data):
        self.intermediatePairs.append(data)
    def run(self, outputQueue):
        self.intermediatePairs.sort(key=self.sortKey)
        print(self.intermediatePairs)
        print()
        for k, vs in itertools.groupby(self.intermediatePairs, key=lambda x: x[0]):
            self.output.update(self.reduceFunc(k, list(map(lambda x: x[1], vs))))
        outputQueue.put(self.output)