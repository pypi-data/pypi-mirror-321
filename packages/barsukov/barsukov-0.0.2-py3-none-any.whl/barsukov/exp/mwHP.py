### BEGIN Dependencies ###
import numpy as np
import sys
from barsukov.exp.exp_utils import *
### END Dependencies

# STATUS: f() finished, nor test it and then add more funcitons

class mwHP:
    def __init__(self, gpib=None, visa_rm=None, logger=None, gpib_card=0, log='default', script=None):
        # Pass the Script object, if available.
        # If Script has no visa_rm or if no Script is passed, you'll need to pass the visa_rm=visa.ResourceManager manually.
        # If Script has no logger or if no Script is passed, you can pass the logger manually.
        # If no logger is passed, will simply print to screen.
        # Change log from 'default' to 'screen', 'file', 'both', 'no'.
        # gpib_card is per default 0. You can change, if you have multiple.
        
        self.script = script
        self.logger = logger
        self.eq_default_log = log
        self.rm = visa_rm
        self.gpib_card = gpib_card
        self.gpib = gpib

        self.msg_deco = f'[mwHP {self.gpib_card}::{self.gpib}]'
        #print( 'visa_rm is ', visa_rm )
        #print( 'script is ', script )
        self.eq = initialize_gpib(self) # This will initialize self.eq = visa.open_resource()
        self.log( f'Initialized: {self.identify()}', log='important' ) # This is the 'welcome message' and a check if communication works.
        
        self.f_digits = 9 # Digits of precision of mw frequency
        self.f_limits = [0.01, 20.5] # Lower and upper GHz limits
        self.p_digits = 1 #TODO -- Digits of precision of mw power
        self.p_limits = [-15.0, 17.0] #TODO -- Lower and upper __ limits
        self.pulsef_digits = 3 # digits in KHz
        self.pulsew_digits = 3 # digits in ms
        self.pulsef_limits = [0.016, 500]
        self.pulsew_limits = [0.001, 65.53] # digits in ms
        self.pulsedc_limits = [0, 100]

    ### BEGIN The definition of the following functions may be specific to this equipment.
    def query(self, cmd):
        return self.eq.query(cmd)

    def write(self, cmd):
        return self.eq.write(cmd)

    def identify(self):
        return str(self.eq.query('*IDN?'))
    ### END The definition of the following functions may be specific to this equipment.

    def log(self, msg, log=None):
        if log is None: log=self.eq_default_log
        log_in_eq(self, msg, log=log)
    ### END These functions could be shared across all equipment.


    def f(self, f=None, log=None, check=False):
    ### Always has a return! Which is frequency in GHz.
    ### f() reads and returns the frequency in GHz.
    ### f(10) writes frequency to 10 GHz.
    ### f(10) returns the frequency that was actually sent to equipment.
    ### f(10, check=True) returns the frequency queried after writing.
    ### Do set log='no' to avoid latency for repeated calls. 
        if log is None: log=self.eq_default_log
        if f is None: 
            try:
                y = self.eq.query('freq?')
                y = float(y)/1e9 # Is the frequency returned in GHz??
                self.log(f'Reading f as {y} GHz.', log=log)
                return y
            except:
                self.log(f'Error while reading Frequency.', log='important')
                return np.nan
        else:
            try:
                x = round(f, self.f_digits) # rounding the digits
                x = max(self.f_limits[0], min(x, self.f_limits[1])) # sets x within f_limits
                self.eq.write(f'freq {x} GHz')
                if check: y = self.f(log='no')
                else: y = x
                print(y, f)
                if abs(y-f)<10.0**(-self.f_digits): self.log(f'Writing f as {x}.', log=log) #################### THIS IS WRONG!!!! IT SHOULD BE abs(y-f)<(10**self.f_digits)
                else: self.log(f'Warning: writing Frequency as {x}, but was asked {f}.', log='important')
                return y
            except:
                self.log(f'Error while writing Frequency as {f}.', log='important')
                return np.nan

    def p(self, p=None, log=None, check=False):
    ### Always has a return! Which is the power in dBm.
    ### p() reads and returns the power in dBm.
    ### p(1) writes power to 1 dBm.
    ### p(1) returns the power that was actually sent to equipment.
    ### p(1, check=True) returns the power queried after writing
    ### Do set log='no' to avoid latency for repeated calls.
        if log is None: log=self.eq_default_log
        if p is None:
            try:
                y = self.eq.query('pow?')
                y = float(y)
                self.log(f'Reading p as {y} dBm.', log=log)
                return y
            except:
                self.log(f'Error while reading Power.', log='important')
                return np.nan
        else:
            try:
                x = round(p, self.p_digits) # rounding the digits
                x = max(self.p_limits[0], min(x, self.p_limits[1])) # sets x within p_limits
                self.eq.write(f'pow {x} dBm')
                if check: y = self.p(log='no')
                else: y = x
                if abs(y-p)<10**(-self.p_digits): self.log(f'Writing p as {x}.', log=log)
                else: self.log(f'Warning: writing Power as {x}, but was asked {p}.', log='important')
                return y
            except:
                self.log(f'Error while writing Power as {p}.', log='important')
                return np.nan

    def output(self, state=None, log=None, check=False):
    ### Always has a return! Which is the state of Output.
    ### output() reads and returns the state of Output.
    ### output(1) writes state of Output to ON.
    ### output(1) returns the state that was actually sent to equipment.
    ### output(1, check=True) returns the state queried after writing
        if log is None: log=self.eq_default_log
        if state is None:
            try:
                y = self.eq.query('output?')
                y = int(y)         
                self.log(f'Output is {y}.')
                return y
            except:
                self.log(f'Error while reading Output.', log='important')
                return np.nan
        else:
            if (state == 1) or (state == 'on') or (state=='ON') or (state=='On'): sstate = 1
            else: sstate = 0
            try:
                self.eq.write(f'output {sstate}')
                if check: y=self.output(log='no')
                else: y = sstate
                if y == state: self.log(f'Output set to {sstate}.')
                else: self.log(f'Warning: Setting Output to {sstate}, but was asked for {state}.')
                return y
            except:
                self.log(f'Error while changing Output state.', log='important')
                return np.nan
    
    #def sweep(self, mode, state=None, step=None, dwell=None, minm=None, maxm=None, log=None, check=False):
        #if log is None: log=self.eq_default_log
        #if (mode == 'pow') or (mode == 'freq'): ### Sweep function can write to power or frequency
            #if state is None: ### sweep(pow) or sweep(freq) reads and returns if the sweep mode is on or off
                #try:
                    #y = self.eq.query(f'{mode} swe?')
                    #y = float(y)
                    #self.log(f'{mode} Sweep state is {y}.')
                    #return y
                #except:
                    #self.log(f'Error while reading {mode} Sweep state.', log='important')
                    #return np.nan
            #else:
                #if (state == 1) or (state == 'on') or (state=='ON') or (state=='On'): sstate = 'swe' ### sweep(pow, 1) or sweep (freq, 1) turns the sweep mode for pow/freq ON
                #else: sstate = 'fix'
                #try:
                    #self.eq.write(f'{mode} {sstate}')
                    #if check: y=self.output(log='no')
                    #else: y = sstate
                    #if y == state: 
                        #self.log(f'{mode} Sweep state set to {sstate}.')
                        #if (step=None) or (dwell=None) or (maxm=None) or (minm=None):
                            #self.log(f'Warning: missing arguements to conduct {mode} Sweep.') ### indicates that while power mode on, sweep
                        #else:
                            #if (mode == 'pow'): level = 'dBm'
                            #elif (mode == 'freq'): level = 'GHz'
                            #dwellunit = 'us' ### is it in microseconds?
                            #self.eq.write(f'{mode} step {step} {level})
                            #self.eq.write(f'{mode} dwel1 {dwell} {dwellunit})
                            #self.eq.write(f'{mode} star {minm} {level}')
                            #self.eq.write(f'{mode} stop {maxm} {level}')
                            ### write checks to see if values are actually written to Output
                            #self.eq.write(f'init imm')
                        #return y                          
                    #else: 
                        #self.log(f'Warning: Setting {mode} Sweep state to {sstate}, but was asked for {state}.')
                        #return y
                #except:
                    #self.log(f'Error while changing {mode} Sweep state.', log='important')
                    #return np.nan
        #else:
            #self.log(f'Warning: mode for sweep was not specified.', log=log)
            #return np.nan




    def pulse(self, f=None, duty=None, log=None):
        if log is None: log=self.eq_default_log
        if f is None and duty is None:
            T = float(self.eq.query('puls:per?')) * 10.0**3
            f = 1.0 / T
            w = float(self.eq.query('puls:widt?')) * 10.0**3
            duty = w / T * 100.0
            y = self.eq.query('pulm:stat?')
            y = int(y)
            x = self.eq.query('pulm:sour?')
            x = x[:-1].lower()
            self.log(f'Pulse Frequency {f} KHz, duty-cycle {duty}%. state {y}, source {x}.', log=log)
            return f, duty
        
        else:
            if f is None and duty is not None:
                duty_write = max(self.pulsedc_limits[0], min(float(duty), self.pulsedc_limits[1]))
                T = float(self.eq.query('puls:per?')) * 10.0**3
                w = duty_write * T / 100.0
                self.eq.write(f'puls:widt {w} ms')

            elif f is not None and duty is None:
                f_write = max(self.pulsef_limits[0], min(float(f), self.pulsef_limits[1]))
                duty_write = 50.0
                T = 1.0 / f
                w = duty_write * T / 100.0
                self.eq.write(f'puls:per {T} ms')
                self.eq.write(f'puls:widt {w} ms')

            elif f is not None and duty is not None:
                f_write = max(self.pulsef_limits[0], min(float(f), self.pulsef_limits[1]))
                duty_write = max(self.pulsedc_limits[0], min(float(duty), self.pulsedc_limits[1]))
                T = 1.0 / f
                w = duty_write * T / 100.0
                self.eq.write(f'puls:per {T} ms')
                self.eq.write(f'puls:widt {w} ms')

            check = self.pulse()
            return check


    #def pulse(self, on_off=None, freq=None, duty_cycle=None, int_ext=None, log=None):
    ### Always has a return! Which is the state, freq, duty cycle, and source of pulse
    ### Frequency in KHz, Duty Cycle in %, source int(ernal) or ext(ernal)
    ### pulse() reads and returns state, frequency, duty cycle, and source of pulse
    ### pulse(1,1,50,int) writes state ON, frequency 1KHz, duty cycle 50%, and internal mode to Pulse
    ### pulse(1,1,50,int) returns the state, frequency, duty cycle, and source that was actually sent to the equipment
    ### pulse(1,1,50,int) returns the state, frequency, duty cycle, and source queried after writing
        #if log is None: log=self.eq_default_log
        #if (on_off is None) and (freq is None) and (duty_cycle is None) and (int_ext is None): 
        ### Accesser Code - returns whats on equipment object
            #try:
                #y = self.eq.query('pulm:stat?')
                #y = int(y)
                #f = float(self.eq.query('puls:freq?')) / 10.0**3
                    # returns in Khz
                #dc = float(self.eq.query('puls:widt?')) * f * 10.0**5
                    # returns in %
                #x = self.eq.query('pulm:sour?')
                #x = x[:-1].lower()
                    # returns in lowercase
                #self.log(f'Pulse state is {y}, frequency {f} KHz, duty-cycle {dc}%, source {x}.', log=log)
                #return [y, f, dc, x]
            #except:
                #self.log(f'Error while reading Pulse state.', log='important')
                #return np.nan
        #else: 
        ### Mutator Code - Writes to equipment object
            #if (on_off == 1) or (on_off == 'on') or (on_off=='ON') or (on_off=='On'): state = 1
            #else: state = 0
            #error = False
            #if (int_ext == 'int') or (int_ext == 'ext') or (int_ext == 'INT') or (int_ext == 'EXT'): 
                ### writes mode (int/ext)
                    #try:
                        #self.eq.write(f'pulm:sour {int_ext}')
                        #y = self.eq.query('pulm:sour?')
                        #y = y[:-1].lower()
                        #if (str(y) == str(int_ext.lower())): self.log(f'Setting Pulse to {int_ext}.', log=log)
                        #else: self.log(f'Warning:Setting Pulse to {y[3]}, but was asked {int_ext}.', log='important')
                    #except: 
                        #self.log(f'Error while changing Pulse Source.', log='important')
                        #return np.nan 
            #elif (int_ext is not None): self.log(f'Error: Invalid Pulse Source.', log='important')
            #if (freq is None) and (duty_cycle is not None): 
            ### if frequency and duty cycle not in ratio, changes duty cycle to acceptable value
                #try:
                    #writeduty_cycle = float(duty_cycle)
                    #writeduty_cycle = max(self.pulsedc_limits[0], min(writeduty_cycle, self.pulsedc_limits[1])) # sets writeduty_cycle within pulsedc_limits
                    #y = float(self.eq.query(f'puls:freq?')) / 1000.0 #returns in KHz
                    #writefreq = y
                    #width = writeduty_cycle * 0.01 / writefreq # units of ms
                    #width = max(self.pulsew_limits[0], min(width, self.pulsew_limits[1]))
                    #wdth = ceil(width * 1000.0) / 1000.0
                    #idth = round(width, self.pulsew_digits)
                    #lf.eq.write(f'puls:widt {width} ms')
               #except:
                   #self.log(f'Error while changing Duty Cycle within limits.', log='important')
                   #error = True
                   #return np.nan              
           #elif (duty_cycle is None) and (freq is not None):
            ### if frequency and duty cycle not in ratio, changes frequency to acceptable value
             #  try:
              #     writeduty_cycle = 50.0
               #    writefreq = round(freq, self.pulsef_digits) # rounding the digits
                #   writefreq = max(self.pulsef_limits[0], min(writefreq, self.pulsef_limits[1])) # sets writeduty_cycle within pulsedc_limits
                 #  print(writefreq)
                  # width = writeduty_cycle * 0.01 / writefreq # units of ms
                #   width = max(self.pulsew_limits[0], min(width, self.pulsew_limits[1]))
                #   width = ceil(width * 1000.0) / 1000.0 
                  #width = round(width, self.pulsew_digits)
                #   print(width)
                #   self.eq.write(f'puls:freq {writefreq} KHz')
                #   self.eq.write(f'puls:widt {width} ms')
              # except:
                #  print(width)
               #    self.log(f'Error while changing Pulse Frequency within limits.', log='important')
                 #  error = True
                  # return np.nan 
           #elif (freq is not None) and (duty_cycle is not None):
            ### writing both duty cycle and frequency
              # writeduty_cycle = float(duty_cycle) # rounding the digits
              # writeduty_cycle = max(self.pulsedc_limits[0], min(writeduty_cycle, self.pulsedc_limits[1])) # sets writeduty_cycle within pulsedc_limits
              # writefreq = round(freq, self.pulsef_digits) # rounding the digits
              # writefreq = max(self.pulsef_limits[0], min(writefreq, self.pulsef_limits[1])) # sets writeduty_cycle within pulsedc_limits
              # try:
                  # width = writeduty_cycle * 0.01 / writefreq # units of ms
                  #width = max(self.pulsew_limits[0], min(width, self.pulsew_limits[1]))
                  # width = ceil(width * 1000.0) / 1000.0
                  # width = round(width, self.pulsew_digits)
                   #self.eq.write(f'puls:freq {writefreq} KHz')
                   #self.eq.write(f'puls:widt {width} ms')
                #xcept: 
                #  self.log(f'Error while writing Duty Cycle.', log='important')
                 #  self.log(f'Error while writing Pulse Frequency.', log='important') 
                  # error = True
                  # return np.nan              
           #y = self.pulse(log='no')
            ### returns the actual parameters written to machine to be compared 
           #if (freq is not None) and (error == False): 
               ### Checker Code
            #   if abs(y[1] - freq)< 10**(-self.pulsef_digits): self.log(f'Writing Pulse Frequency as {y[1]}.', log=log)
             # else: self.log(f'Warning:Writing Pulse Frequency as {y[1]}, but was asked {freq}.', log='important')
           #if (duty_cycle is not None) and (error == False):
                ### Checker Code
             #  if abs(y[2] - duty_cycle)<10**(-3): self.log(f'Writing Pulse duty cycle as {y[2]}.', log=log)
              # else: self.log(f'Warning:Writing Pulse duty cycle as {y[2]}, but was asked {duty_cycle}.', log='important')
           #if (on_off is not None):
            #   try:
             #      self.eq.write(f'pulm:stat {on_off}')
              #     x = self.eq
               #    y = self.pulse(log='no')
                #   if y[0] == state: self.log(f'Pulse state set to {on_off}.')
                 #  else: self.log(f'Warning: Setting Pulse state to {sstate}, but was asked for {on_off}.')
                #xept:
                #   self.log(f'Error while changing Pulse state.', log='important')
                 #  error = True
                  # return np.nan
           #if (error == False): return y
           #else: return np.nan

