from barsukov.time import *
from barsukov.logger import Logger

import sys
import os

class Script():
    def __init__(self,
        ### Please ALWAYS specify the following:
        operator='Anon', # ib, Rundong, Sasha, Ameerah, Alex, or AlexH if ambiguous  
        station='No Stn', # qd, ppms, mseppms, data, orange, ...
        sample='No Sample', # Use sample name from the sample table, e.g. "cro2410a1" or "yig2207"
        description='No Description', # Briefly: what are you doing. Sets the folder name.
        # i.e. 'Testing modulation' or 'fH OOP long average'
        project_folder = os.getcwd(), # Full path to your project folder. Please follow this convention:
        # D:/Rundong/Projects/AFM sims/2024-07-06 Autooscillations
        # Will grab the current directory if not specified.

        ### Optional:
        log='both', # This is the default log setting which will be passed to the logger.
            ### It will be overriden by other objects,
            ### which in turn will be overriden by methods.
            ### Choose here and everywhere from screen, file, both, no.

        ### Usually, it's better not to change these:
        log_full_folder_path=None,
        log_full_file_path=None 
        ):
        
        self.operator = operator
        self.station = station
        self.sample = sample
        self.description = description
        self.project_folder = project_folder

        self.rm = None
        
        ### Creating the sub-project folder
        self.folder_name = date() + '_' + self.station + '_' + self.operator + '_' + self.sample + '_' + self.description
        self.full_folder_path = os.path.join(self.project_folder, self.folder_name)
        os.makedirs(self.full_folder_path, exist_ok=True)

        ### Starting the logger
        if log_full_folder_path is None:
            self.logger = Logger(
                description=self.operator + '_' + self.description,
                full_file_path=log_full_file_path,
                log=log, # Script.log becomes Logger's default
                start_file=True)
        else:
            self.logger = Logger(
                description=self.operator + '_' + self.description,
                full_folder_path=log_full_folder_path,
                full_file_path=log_full_file_path,
                log=log, # Script.log becomes Logger's default
                start_file=True) 
        
        self.logger.log(f'Script object initialized. Logger started.', log='both')
        
    def log(self, msg, log='default'): # default means the default of the logger
        self.logger.log(msg, log=log)
    

### BEGIN: Equipment related stuff

    def init_rm(self):
    # Imports pyvisa as method library #
        import pyvisa as visa # ----------------XXX Can this be done like this??????????????
        try: 
            self.rm = visa.ResourceManager()
        except:
            self.rm = None
            self.log('Script could not import pyvisa.', log='important')
            sys.exit()
        self.log(f'Script started pyvisa.ResourceManager.', log='both')
        return self.rm

### BEGIN Equipment devices
    
    def mwHP(self, **kwargs):
        from barsukov.exp.mwHP import mwHP as eq
        return eq(**kwargs, script=self, logger=self.logger)
