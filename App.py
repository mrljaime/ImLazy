#! /usr/bin/env python 
# --*-- encoding: utf-8 --*--

from stamper.DirectoryReader import DirectoryReader 
from stamper.DBManager import DBManager
from stamper.PaymentCompanyDao import PaymentCompanyDao
from stamper.Execution import Execution
from arg import args as arguments
from config import config
from logger import logging

class App():
    
    def run(self):
        db_manager = DBManager(host=config.get("db", "host"), 
                               user=config.get("db", "user"), 
                               password=config.get("db", "password"), 
                               database=config.get("db", "database"))
        db_manager.connect()
        payment_company_dao = PaymentCompanyDao(db_manager)
        executable = Execution()
    
        directoryReader = DirectoryReader(arguments.directory)
        directoryReader.read()
    
        directories = directoryReader.get_directories()
    
        for directory in directories.keys():
            # Directory variable means root variable, that means that it is the worked_outsource parent
            rfc = directory[:12]
#            print(rfc)
#            print(payment_company_dao.get_by_rfc(rfc))
            i_payment_company = payment_company_dao.get_by_rfc(rfc) or ("None")
            i_directories = directories[directory]
        
            # Check if this has dependencies. It has, theres time to start stamping with subdirectories, otherwise lets
            if 0 < len(i_directories):
                for i_i_directory in i_directories:
                    i_i_directory = i_i_directory.replace(" ", "")
                    outsource_rfc = i_i_directory[:12]
                    # Execute command
                    executable.do(stamped=False, 
                                  is_outsource=True, 
                                  rfc=rfc, 
                                  rfc_outsource=outsource_rfc, 
                                  payment_company_id=i_payment_company[0])
    
            else:
                executable.do(stamped=False, 
                              is_outsource=False,
                              rfc=rfc, 
                              payment_company_id=i_payment_company[0])