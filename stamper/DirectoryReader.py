# --*-- encoding: utf-8 --*--

import os
from logger import logging

class DirectoryReader():
    
    root = ""
    directories = {}
    
    def __init__(self, root):
        self.root = root
        
    def read(self, recursive=True):
        self._read(directory=self.root, recursive=True, root_dir=True)
        
    def _read(self, directory, relative_path="", recursive=True, root_dir=False):
        # Avoid unexpected results
        if os.path.isdir(directory) is False:
            #print("Nada por hacer")
            logging.debug("Nothing to do")

            return
        
        for i_directory in os.listdir(directory):
            #print(i_directory)
            logging.debug(i_directory)
            
            if "recibos" == i_directory and root_dir is False:
                #print("Ya llegué a los recibos")
                logging.debug("All is done in this path")

                continue;
                
            if "recibos" == i_directory and root_dir is True:
                logging.debug("Is on root directory, let's try to check if has archives")
                self.directories[i_directory] = []
                
                continue

            if ".DS_Store" == i_directory:
                
                logging.debug("There's no directory here")
                
                continue
            
            if "txt" in i_directory:
                #print("Ya llegue a los archivos")
                logging.debug("There's in the final folder")
                break
            
            if "pdf" in i_directory:
                logging.debug("There's in the final folder")
                break

            if "xml" in i_directory:
                logging.debug("There's in the final folder")
                break
                
            if root_dir is True:
                logging.info("Root directory")
#                self.directories[i_directory] = {i_directory: i_directory}
                self.directories[i_directory] = []
            
            if root_dir is False:
                logging.info("Relative path: %s" % relative_path)
                self.directories[relative_path].append(i_directory)
            
            if recursive is True:
                i_dir = directory + "/" + i_directory
                i_dir = i_dir.replace("//", "/")
                self._read(i_dir, root_dir=False, relative_path=i_directory)
                
    def get_directories(self):
        return self.directories
                            
    def __repr__(self):
        return str(self.directories)
        