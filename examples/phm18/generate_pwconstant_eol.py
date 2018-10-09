# Copyright 2018 United States Government as represented by the Administrator of
# the National Aeronautics and Space Administration. No copyright is claimed in
# the United States under Title 17, U.S. Code. All Other Rights Reserved.

# The Stochastic Reduced Order Models with Python (SROMPy) platform is licensed
# under the Apache License, Version 2.0 (the "License"); you may not use this
# file except in compliance with the License. You may obtain a copy of the
# License at http://www.apache.org/licenses/LICENSE-2.0.

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import numpy as np

from SROMPy.postprocess import Postprocessor
from SROMPy.srom import SROM
from SROMPy.target import SampleRandomVector

'''
Script to generate piecewise constant SROM approximation to EOL and compare it 
with the Monte Carlo solution - step 3. Uses the stored EOL model outputs 
from step 2 and the stored input SROM from step 1.
'''

mc_eol_file = "mc_data/eol_samples_MC.txt"

sromsize = 20

srom_eol_file = "srom_data/srom_eol_m" + str(sromsize) + ".txt"
srom_input_file = "srom_data/srom_m" + str(sromsize) + ".txt"

#Get MC EOL samples
MC_eols = np.genfromtxt(mc_eol_file)

#Get SROM EOL samples & probabilities from input srom
srom_eols = np.genfromtxt(srom_eol_file)
srom_probs = np.genfromtxt(srom_input_file)[:,-1]  #probs in last column

#Make MC random variable & SROM to compare
eol_srom = SROM(sromsize, dim=1)
eol_srom.set_params(srom_eols, srom_probs)
eol_mc = SampleRandomVector(MC_eols)

pp = Postprocessor(eol_srom, eol_mc)
pp.compare_CDFs(variablenames=["EOL"])
