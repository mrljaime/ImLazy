# --*-- encoding: utf-8 --*--

from logger import logging
from config import config 
from arg import args as arguments
import subprocess

class Execution():
    
    COMMAND = config.get("stamper", "commmand")
    
    def __init__(self):
        self.root = arguments.directory
    
    def do(self, rfc, payment_company_id, stamped=False, is_outsource=False, is_asimilated=False,rfc_outsource=""):
        dir = self.root + "/" + rfc 
        options = ""
        
        if stamped is True:
            options += "-s 1 "

        if is_outsource is True:
            dir += "/" + rfc_outsource
            options += " -o 1 "
            
        dir = dir.replace("//", "/")
            
        shell = "%s %s %s/recibos %s %s %s" % (self.COMMAND, dir, dir, payment_company_id, rfc_outsource, options)
        logging.info("Execute shell: %s" % shell)
        
        p = subprocess.Popen(shell, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        logging.info("Returning call: ")
        logging.info(output)
        