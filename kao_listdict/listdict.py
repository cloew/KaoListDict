from kao_decorators import proxy_for

@proxy_for("items", ["__iter__", "__contains__", "__len__", "__getitem__", "__repr__"])
class ListDict:
    """ Represents a Dictionary that wraps all its values in a list """
    
    def __init__(self):
        """ Initialize the dictionary to be empty """
        self.items = {}
        
    def __setitem__(self, key, value):
        """ Set the given key to contain the given value """
        if key not in self.items:
            self.items[key] = []
        self.items[key].append(value)