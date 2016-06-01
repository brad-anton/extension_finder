"""
InternetExplorer.py -
@brad_anton

"""
from Browser import Browser
from Extension import Extension

from os import path, walk
try:
    import _winreg 
except ImportError:
    pass

class InternetExplorer(Browser):
    def find(self):
        """Searches for the Browser and returns True 
        if it finds its"""
        return path.exists(self.os.IE)
        
    def extensions(self):
        """Main method which handles the processing of extentsions
        """
        
        extensions = []
        
        if self.find():
            """Internet Explorer has a bunch of registry keys for 
            extensions, so we'll hold two connections open for the
            querying"""
            hklm = _winreg.ConnectRegistry(None, _winreg.HKEY_LOCAL_MACHINE)
            hkcu = _winreg.ConnectRegistry(None, _winreg.HKEY_CURRENT_USER)
            
            for registry_key in self.os.IE_REGKEYS:
            
                key = None
                idx = 0
            
                if registry_key['hive_str'] == 'HKLM':
                    hive = hklm
                elif registry_key['hive_str'] == 'HKCU':
                    hive = hkcu
                
                try:
                    key = _winreg.OpenKey(hive, registry_key['path'])
                    while True:
                        if registry_key['type'] == 'key':
                            entry = _winreg.EnumKey(key, idx)
                            clsid_key = '{}\\{}'.format(registry_key['path'], entry)
                            
                            """For registry keys of type 'key', we open the key
                            and attempt to find a specific ClsidExtension value 
                            to use as the CLSID. If it fails, we just use the 
                            key name itself.
                            """
                            clsid = self.__get_clsid(hive, clsid_key)
                            if not clsid:
                                clsid = entry
                        else:
                            clsid = _winreg.EnumValue(key, idx)[0]
                          
                        id, name, dll = self.__lookup_clsid(clsid)
                        #e = Extension(self.os.IE_NAME, name, None, dll, id)
                        e = Extension(name, None, dll, id)
                        extensions.append(e.todict())
                        
                        idx += 1
                except WindowsError:
                    pass
           
        else:
           print '[!] Could not find Internet Explorer Extensions!'

        return extensions
      
    def __get_clsid(self, hive, key):
        """Gets a CLSID from the IE Extensions registry key
        """
        clsid = None
        try:
            k = _winreg.OpenKey(hive, key)
            clsid = _winreg.QueryValueEx(k, 'ClsidExtension')[0]
        except WindowsError:
            pass
            
        return clsid
                    
    def __lookup_clsid(self, clsid):
        """Look up a CLSID in the Windows Registry and 
        returns its name and DLL path
        """
        name = None
        dll = None
        try:
            name_key =  '{}\\{}'.format(self.os.CLSID,clsid)
            k = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, name_key)
            name = _winreg.QueryValue(k, None)
            
            dll_key =  '{}\\InProcServer32'.format(name_key)
            k = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, dll_key)
            dll = _winreg.QueryValueEx(k, None)[0]
        except WindowsError:
            pass
            
        return clsid, name, dll
