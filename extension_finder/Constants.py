"""
Constants.py
@brad_anton

Constant variables.

Path names are prefexed by HOMEDIR unless starting 
with a slash

"""

from enum import Enum

import platform


class RegistryKey:
    def __init__(self, path, type='value'):
        from _winreg import HKEY_LOCAL_MACHINE, HKEY_CURRENT_USER
        self.type = type
        self.hive = None
        self.hive_str = path[:4]
        self.path = path[5:]
        
        if self.hive_str == 'HKLM':
            self.hive = HKEY_LOCAL_MACHINE
        elif self.hive_str == 'HKCU':
            self.hive = HKEY_CURRENT_USER


class MacBrowsers(Enum):
    SLASH = '/'
    CHROME = '/Applications/Google Chrome.app'
    CHROME_NAME = 'Chrome - MacOSX'
    CHROME_EXTENSIONS = 'Library/Application Support/Google/Chrome/Default/Extensions'
    CHROME_EXTENSIONS_PREFS = 'Library/Application Support/Google/Chrome/Default/Preferences'

    SAFARI = '/Applications/Safari.app'
    IE = None

class WinBrowsers(Enum):
    SLASH = '\\'
    CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    CHROME_NAME = 'Chrome - Windows'
    CHROME_EXTENSIONS = r'AppData\Local\Google\Chrome\User Data\Default\Extensions'
    CHROME_EXTENSIONS_PREFS = r'AppData\Local\Google\Chrome\User Data\Default\Preferences'
    
    
    if platform.system() == 'Windows':
        import _winreg
        IE = r'C:\Program Files\Internet Explorer\iexplore.exe'
        IE_NAME = 'Internet Explorer'
        IE_BHO = RegistryKey(r'HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\Browser Helper Objects').__dict__
        IE_BHO_64 = RegistryKey(r'HKLM\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\Browser Helper Objects').__dict__
        IE_URL_SEARCHHOOKS = RegistryKey(r'HKCU\Software\Microsoft\Internet Explorer\UrlSearchHooks').__dict__
        IE_TOOLBAR = RegistryKey(r'HKLM\Software\Microsoft\Internet Explorer\Toolbar').__dict__
        IE_TOOLBAR_64 = RegistryKey(r'HKLM\Software\Wow6432Node\Microsoft\Internet Explorer\Toolbar').__dict__
        IE_EXPLORERBAR_CU = RegistryKey(r'HKCU\Software\Microsoft\Internet Explorer\Explorer Bars').__dict__
        IE_EXPLORERBAR_LM = RegistryKey(r'HKLM\Software\Microsoft\Internet Explorer\Explorer Bars').__dict__
        IE_EXPLORERBAR_CU64 = RegistryKey(r'HKCU\Software\Wow6432Node\Microsoft\Internet Explorer\Explorer Bars').__dict__
        IE_EXPLORERBAR_LM64 = RegistryKey(r'HKLM\Software\Wow6432Node\Microsoft\Internet Explorer\Explorer Bars').__dict__
        IE_EXTENSIONS_CU = RegistryKey(r'HKCU\Software\Microsoft\Internet Explorer\Extensions', 'key').__dict__
        IE_EXTENSIONS_LM = RegistryKey(r'HKLM\Software\Microsoft\Internet Explorer\Extensions', 'key').__dict__
        IE_EXTENSIONS_CU64 = RegistryKey(r'HKCU\Software\Wow6432Node\Microsoft\Internet Explorer\Extensions', 'key').__dict__
        IE_EXTENSIONS_LM64 = RegistryKey(r'HKLM\Software\Wow6432Node\Microsoft\Internet Explorer\Extensions', 'key').__dict__
        # New For Win8: 
        # https://msdn.microsoft.com/en-us/library/dd433050(v=vs.85).aspx
        IE_EXTENSIONS_ACTIVEX = RegistryKey(r'HKCU\Software\Microsoft\Windows\CurrentVersion\Ext\Stats', 'key').__dict__
        
        
        IE_REGKEYS = [  IE_BHO, 
                        IE_BHO_64, 
                        IE_URL_SEARCHHOOKS, 
                        IE_TOOLBAR, 
                        IE_TOOLBAR_64, 
                        IE_EXPLORERBAR_CU,
                        IE_EXPLORERBAR_LM,
                        IE_EXPLORERBAR_CU64,
                        IE_EXPLORERBAR_LM64,
                        IE_EXTENSIONS_CU,
                        IE_EXTENSIONS_LM,
                        IE_EXTENSIONS_CU64,
                        IE_EXTENSIONS_LM64,
                        IE_EXTENSIONS_ACTIVEX ]
                    
        CLSID = r'SOFTWARE\Classes\CLSID'



        
        