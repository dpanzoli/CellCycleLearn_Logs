from os import listdir
import os
from os import remove
from os.path import isfile, join
import re


for f in listdir("./logsUPSCUFR/"):
        if isfile(join("./logsUPSCUFR/", f)):
            tab=f.split("_")
            print(f)
            if tab[2] == "event.log":
                if not os.path.exists('C:\\Users\\stage\\Desktop\\Stage_Marvyn\\CellCyclelearn_Logs\\logsCecyle\\logsUPSCUFR\\'+tab[0]+"_"+tab[1]+"_input.log"):
                    remove('C:\\Users\\stage\\Desktop\\Stage_Marvyn\\CellCyclelearn_Logs\\logsCecyle\\logsUPSCUFR\\'+str(f))
            else:
                    if not os.path.exists('C:\\Users\\stage\\Desktop\\Stage_Marvyn\\CellCyclelearn_Logs\\logsCecyle\\logsUPSCUFR\\'+tab[0]+"_"+tab[1]+"_event.log"):
                        remove('C:\\Users\\stage\\Desktop\\Stage_Marvyn\\CellCyclelearn_Logs\\logsCecyle\\logsUPSCUFR\\'+str(f))


