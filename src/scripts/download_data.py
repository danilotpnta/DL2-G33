# pip install openxlab #Install
# pip install -U openxlab #Upgrade

import subprocess
import sys

# Install the package using pip
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'openxlab'])

# Upgrade the package using pip
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'openxlab'])

import openxlab
Access_Key = 'egarpdrablnlympor5nw'
Secret_Key = 'kporjgbyle38rjqajjjrwpxooaokmxn9qbglzpw5'
openxlab.login(ak=Access_Key, sk=Secret_Key) #Log in and enter the corresponding AK/SK

from openxlab.dataset import info
info(dataset_repo='GMAI/SA-Med2D-20M') #Dataset information viewing

from openxlab.dataset import query
query(dataset_repo='GMAI/SA-Med2D-20M') #View Dataset File List

from openxlab.dataset import get
data_path = '/Users/datoapanta/Desktop/DL2-G33/src/data'
get(dataset_repo='GMAI/SA-Med2D-20M', target_path=data_path)  # Dataset download

from openxlab.dataset import download
download(dataset_repo='GMAI/SA-Med2D-20M',source_path='/README.md', target_path=data_path) #Dataset file download