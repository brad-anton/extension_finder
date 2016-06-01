"""
Browser.py -
@brad_anton

"""

from os import path

class Browser:
    def __init__(self, os, dir=None):
        if not os:
            raise ValueError('Browser created without a OS defined!')
            
        self.os = os
        
        if dir:
            self.directory = dir
        else:
            self.directory = path.expanduser('~')
        
    def find(self):
        """Searches for the Browser and returns True 
        if it finds its"""
        # Override Me 
        pass
    
    def extensions(self):
        """Main method which handles the processing of extentsions
        """
        # Override Me 
        pass
    

