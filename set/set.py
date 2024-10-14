class Set:
    def __init__(self):
        self.element_container = []

    def is_empty(self):
        return len(self.element_container) == 0

    def add(self, param):
        if param not in self.element_container:
            self.element_container.append(param)

    def add_all(self, *element):
        for element in element:
            self.add(element)

    def size(self):
        return len(self.element_container)

    def remove(self, element):
        if self.is_empty():
            raise KeyError('Set is Empty')
        if element not in self.element_container:
            raise KeyError(f"{element} Not Found in set")
        self.element_container.remove(element)

    def clear(self):
        self.element_container = []

    def contains(self, element):
        if self.is_empty():
            raise KeyError('Set is Empty')
        if element not in self.element_container:
            raise KeyError(f"{element} Not Found in set")
        return True
