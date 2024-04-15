import subprocess
import sys
import os

# Install the package using pip
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gdown'])

import gdown

url = 'https://drive.google.com/uc?id=1ARiB5RkSsWmAB_8mqWnwDF8ZKTtFwsjl'
checkpoint_dir = '../data/checkpoints/'
os.makedirs(checkpoint_dir, exist_ok=True)

output = checkpoint_dir + 'sam-med2d_b.pth'
gdown.download(url, output, quiet=False)
