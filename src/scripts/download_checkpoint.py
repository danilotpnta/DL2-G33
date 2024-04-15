import subprocess
import sys

# Install the package using pip
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gdown'])

import gdown

url = 'https://drive.google.com/uc?id=1ARiB5RkSsWmAB_8mqWnwDF8ZKTtFwsjl'
output = '../data/checkpoints/sam-med2d_b.pth'
gdown.download(url, output, quiet=False)
