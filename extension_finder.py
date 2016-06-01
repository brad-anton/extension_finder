"""
extension_finder.py -
@brad_anton

Simple Script to identify which browser extensions are installed on a system. 

"""
from extension_finder.Finder import Finder

if __name__ == '__main__':
    f = Finder()
    f.print_extensions()

