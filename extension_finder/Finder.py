"""
Finder.py -
@brad_anton

Simple Script to identify which browser extensions are installed on a system. 

"""
import platform 
from tabulate import tabulate

from Constants import MacBrowsers, WinBrowsers
from Browsers.Chrome import Chrome
from Browsers.InternetExplorer import InternetExplorer


class Finder:
    def __init__(self, directory=None):
        operating_system = platform.system()
        
        self.os = None
        
        if operating_system == 'Darwin':
            self.os = MacBrowsers
        elif operating_system == 'Windows':
            self.os = WinBrowsers
        else:
            print "[!] Unsupported Operating System!!"
            return
        
    def print_extensions(self):
        c = Chrome(self.os)
        print tabulate(c.extensions(), headers="keys")

        if self.os == WinBrowsers: 
            i = InternetExplorer(self.os)
            print tabulate(i.extensions(), headers="keys")

        
if __name__ == '__main__':
    f = Finder()
    f.print_extensions()

