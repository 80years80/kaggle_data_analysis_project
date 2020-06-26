import pandas as pd
import numpy as np
import os
import subprocess
from kaggle.api.kaggle_api_extended import KaggleApi
# Enabling Kaggle API
api = KaggleApi()
api.authenticate()
# Directory path that file will be sent to
saveTo = '/home/pi/kaggle_data_analysis_project/tempdata'
#file_name for downloading
name = 'WoW Demographics.csv'
#FOR BETTER PRACTICE LATER:
#WILL RENAME FILE VIA BASH COMMANDS
#Download dataset as csv via API
api.dataset_download_file('avenn98/world-of-warcraft-demographics', name, path=saveTo) #Should be csv
#Now restriving the file we do not know the name of
#Set directory we know we saved it to, make home directory path
owd = '/home/pi/kaggle_data_analysis_project'
os.chdir(saveTo)
#There should be only one file in the directory, ls gets us the name
os.system('ls')
#get the name as a bytes, since ls used will have a newline
returned_output = subprocess.check_output('ls')
#decode into a string.
#Remove newline; assuming no kaggle sets have newlines in the name
#Should hold since all non-letters become ascii hex
# https://ascii.cl/ 
#newline in ASCII is Symbol = LF; Hex = 0A; Dec = 10
#Should be fine as is. 
fileName = returned_output.decode("utf-8").rstrip('\n')
#command string to rename file as it was entered but without spaces
name = name.replace(" ", "")
cmd = 'mv ' + fileName + ' ' + name
#get the full path now by combing path and name strings
fullPath = saveTo + '/' + name
#Enter command to rename file
os.system(cmd)     
#Return to home directory to end as good practice
os.chdir(owd)
#Save as dataframe for analysis, have it open the full file path.
df = pd.read_csv(fullPath)