"""
coral_model - interface

@author: Gijs G. Hendrickx

"""
import os

cwd = os.getcwd()

from coral_model.core import Coral
from coral_model.loop import Simulation

base_dir = os.path.join('C:\\','Users','perepely', 'Coral_model',
                        'Ratios')
# define the basic Simulation object, indicating already here the type of hydrodynamics
runTrans = Simulation(mode='Transect')
# set the working directory and its subdirectories (input, output, figures)
runTrans.set_directories(os.path.join(base_dir,'Run_26_10_massive2'))
# read the input file with parameters (processes, parameters,constants, now all in "constants")
runTrans.read_parameters(file='coral_input.txt',folder=runTrans.input_dir)
# environment definition
runTrans.environment.from_file('light', 'TS_PAR.txt',folder=runTrans.input_dir)
runTrans.environment.from_file('temperature', 'TS_SST.txt',folder=runTrans.input_dir)
runTrans.environment.from_file('storm', 'TS_stormcat2.txt',folder=runTrans.input_dir)

# time definition
runTrans.environment.set_dates(start_date = '2000-01-01' , end_date = '2100-01-01' )

# hydrodynamic model
# settings for a 1D idealized transect using fixed currents and Soulsby
# orbital velocities depending on stormcat and depth
runTrans.hydrodynamics.working_dir = runTrans.working_dir
runTrans.hydrodynamics.mdu = os.path.join('input','TS_waves.txt')
runTrans.hydrodynamics.config = os.path.join('input', 'config.csv')
runTrans.hydrodynamics.initiate()
#check
print(runTrans.hydrodynamics.settings)
# define output
runTrans.define_output('map', fme=False)
runTrans.define_output('his', fme=False)
# initiate coral
coral = Coral(runTrans.constants,.125, .125, .1, .1, .2, 0.8)

coral = runTrans.initiate(coral)
# simulation
runTrans.exec(coral)
# finalizing
runTrans.finalise()
# done
