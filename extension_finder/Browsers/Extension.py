"""
Extension.py - Just to standardize the extension information
@brad_anton

"""

class Extension:
    def __init__(self, name, version, path, id):
        self.name = name
        self.version = version
        self.path = path
        
        """Just about every browser creates some sort
        of unique identifier for the extension
        """
        self.id = id

    def todict(self):
        result = {}
        for key in self.__dict__:
            if self.__dict__[key]: result[key] = self.__dict__[key]
        return result 

