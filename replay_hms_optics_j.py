#!/usr/bin/env python
import sys
import os
import subprocess
#import ROOT
#from ROOT import gROOT


oRuns=[4805]#,4805,4806,4807,4808,4809,4810,4811,4812,4813,4814,4815,4816,4817,4821,4822,4824,4825]

#oRuns=[10790,10793,10794,10795]

#oRuns=[10301,10302,10303,10304,10305,10306,10307,10308,10309,10311,10312,10313,10314,10326,10327,10328,10329,10330,10331,10332,10333]
                                                                                                                                                                                                                  
 #oRuns=[10786]

#oRuns=[10776,10779,10780]

#oRuns=[10786,10776,10779,10780,10790,10793,10794,10795]

#oRuns=[9787,9788,9789]

#Loop optics runs
for ii in oRuns:
        subprocess.call("./hcana -b -q 'SCRIPTS/HMS/PRODUCTION/replay_production_hms_coin_all.C(%d,50000)'" % (ii), shell=True)
