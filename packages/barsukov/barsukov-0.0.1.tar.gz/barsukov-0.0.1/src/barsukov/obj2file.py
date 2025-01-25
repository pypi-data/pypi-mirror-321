# This is unfinished


#import pickle
import os
#import glob

import obj_name, time_stamp

class Obj2File:
    def __init__(self, logger=None, log='default', script=None):
        self.script = script
        self.logger = logger
        self.default_log = log
        self.msg_deco = f'[Obj2File]'

        if self.logger is None:
            try: self.logger = self.script.logger
            except: pass

        self.mtj_calib_directory = '/Users/alexandrakorotneva/Desktop/2024-11-18 obj import test'
        self.tosave = {}


    def log(self, msg, log=None):
        if log is None: log = self.default_log
        if self.logger is not None:
            try:
                self.logger.log(f'{self.msg_deco} {msg}', log=log)
                return
            except: pass
        print(f'{time_stamp()} {self.msg_deco} {msg}')
        
    def save(self, obj, directory=None, full_file=None, short_file=None, log='default'):
        if full_file is None:
            if directory is None: directory = self.script.full_folder_path #current measurement folder
            if short_file is None: short_file = f'{time_stamp()}_{obj_name(obj)}.pkl'
            full_file = os.path.join(directory, short_file)
        try:
            with open(full_file, 'wb') as file:
                pickle.dump(obj, file)
                self.log(f'Object {obj_name(obj)} is written to file {full_file}.', log=log)
        except:
            self.log('Error: could not write object to file.', log='important')

    def load(self, directory=None, full_file=None, short_file=None, log='default'):
        if full_file is None:
            if directory is None:
                directory = self.script.full_folder_path
            if short_file is None:
                files = [f for f in glob.glob(os.path.join(directory, '*.pkl'))]
                short_file = files[0]
            full_file = os.path.join(directory, short_file)
            
        try:
            with open(filepath, 'rb') as file:
                toload = pickle.load(file)
                self.log(f'Object is uploaded from file {full_file}.', log=log)
        except:
            self.log('Error: could not upload object from file.', log='important')        
        return toload

 
    

    def mtj_fieldcalib(self, directory=None, upd=False, log='default', spl_ind=None):
        if directory is None: directory = self.mtj_calib_directory
        else:
            if upd: 
                self.mtj_calib_directory = directory
                self.log(f'MTJ station field calibration directory has been updated to {directory}', log='important')

        files = [f for f in glob.glob(os.path.join(directory, '*.pkl'))]
        if len(files)==1:
            short_file = files[0]
        else:
            ##

        full_file = os.path.join(directory, short_file)
        splines = self.load(full_file=full_file, log=log)

        if spl_ind is None:
            return: splines
        elif spl_ind=='c':
            return: splines['cheap_to_H']
        elif spl_ind=='v':
            return: Vsplines['V_to_H']
        elif spl_ind=='h':
            return: splines['H_to_V']

    def pack_tosave(self, obj, obj_name=None, overwrite=False, save=False):
        #prepares a dictionary {'obj name':obj, ...}
        tosave = self.tosave
        if obj_name is None: obj_name = obj_name(obj)
                
        if overwrite:
            tosave.update({obj_name : obj})
        else: 
            add = tosave.setdefault(obj_name, obj) #for already excisting name returns corresponding element and doesn't overwrite
            if add!=obj:
                print(f'Overwriting attempt!')
       
        self.tosave = tosave
        if save:
            self.save(tosave)
        return tosave

