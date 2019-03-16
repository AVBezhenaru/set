class PowerSet:

    def __init__(self):
        self.init = {}
        self.slots = []

    def size(self):
        return len(self.init)

    def put(self, value):
        if self.get(value) is False:
            self.init[value] = value
            self.slots = list(self.init.keys())

    def get(self, value):
        if value in self.init:
            return True
        return False

    def remove(self, value):
        if self.get(value) is True:
            del self.init[value]
            self.slots = list(self.init.keys())
            return True
        return False

    def intersection(self, set2):
        result = PowerSet()
        if set2.init != {} and self.init != {}:

            for key in self.init:
                c = key
                for key in set2.init:
                    d = key
                    if c == d:
                        result.put(c)

        return result

    def union(self, set2):
        result = PowerSet()
        for key in self.init:
            result.put(key)

        for key in set2.init:
            result.put(key)

        return result

    def difference(self, set2):
        result = PowerSet()
        for key in self.init:
            a = set2.get(key)
            if a is False:
                result.put(key)

        return result

    def issubset(self, set2):
        for key in set2.init:
            a = self.init.get(key)
            if a is None:
                return False

        return True