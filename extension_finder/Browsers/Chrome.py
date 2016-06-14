"""
Chrome.py -
@brad_anton

"""
from Browser import Browser
from Extension import Extension

from os import path, walk
import json

class Chrome(Browser):
    def find(self):
        """Searches for the Browser and returns True 
        if it finds its"""
        return path.exists(self.os.CHROME)
        
    def extensions(self):
        """Main method which handles the processing of extentsions
        """
        
        result = None
        
        if self.find():
            try:
                result = self.__check_preferences_json('{}{}{}'.format(self.directory, 
                    self.os.SLASH, 
                    self.os.CHROME_EXTENSIONS_PREFS)) 
            except (KeyError, IOError):
                print '[+] Could not parse the Chrome Preferences JSON, falling back to extensions directory' 
                result = self.__check_app_directory('{}{}{}'.format(self.directory, 
                    self.os.SLASH, 
                    self.os.CHROME_EXTENSIONS))
        else:
           print '[!] Could not find Chrome Extensions!'

        return result
        
    def __check_preferences_json(self, preferences):
        """Pulls Extension information out of the preferences file
        """
        extensions = []
        with open(preferences, 'rb') as f:
            prefs_json = json.load(f)

            extensions_json = prefs_json['extensions']['settings']
            for extension in extensions_json.iterkeys():
                name = None
                version = None
                if 'manifest' in extensions_json[extension]:
                    name = extensions_json[extension]['manifest']['name']
                    version = extensions_json[extension]['manifest']['version']
                   
                #e = Extension(self.os.CHROME_NAME, name, version, None, extension)
                e = Extension(name, version, None, extension)
                extensions.append(e.todict())
        
        return extensions
    
    def __process_manifest_json(self, fullpath):
        """The manifest.json files contain less information
        then the Preferences files, so we'll use this menthod
        on if the preferences file is unavaible"""
        extension = fullpath.split(self.os.SLASH)[-3]

        if path.isfile(fullpath):
            with open(fullpath, 'rb') as f:
                manifest = json.load(f)

            name = manifest['name'] 
            version = manifest['version']
    
        return name, version, extension
    
    def __check_app_directory(self, extension_dirs):
        """Checks each directory in self.dirs for stuff
        """
        extensions = []
        
        for root, dirs, files in walk(extension_dirs):
            for f in files:
                if f == 'manifest.json':
                    manifest = path.join(root, f)
                    name, version, extension = self.__process_manifest_json(manifest)
                    if name[0] == '_':
                        # Check locale for more friendlier name
                        locale_paths = [ '_locales{0}en_US{0}messages.json'.format(self.os.SLASH),
                            '_locales{0}en{0}messages.json'.format(self.os.SLASH)]
                        for locale_path in locale_paths:
                            locale_json = path.join(root, locale_path)
                            if path.isfile(locale_json):
                                with open(locale_json, 'rb') as f:
                                    locale_manifest = json.load(f)
                                    if 'appName' in locale_manifest:
                                        if 'message' in locale_manifest['appName']:
                                            name = locale_manifest['appName']['message']
                                    elif 'extName' in locale_manifest:
                                        if 'message' in locale_manifest['extName']:
                                            name = locale_manifest['extName']['message']
                                    elif 'app_name' in locale_manifest:
                                        if 'message' in locale_manifest['app_name']:
                                            name = locale_manifest['app_name']['message']
                    
                    #e = Extension(self.os.CHROME_NAME, name, version, None, extension)
                    e = Extension(name, version, None, extension)
                    extensions.append(e.todict())
                    
        return extensions

