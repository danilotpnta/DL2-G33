import subprocess
import sys
import os
import gdown

def install_or_update_gdown():
    try:
        import gdown
    except ImportError:
        # If gdown is not installed, this block will install it
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gdown'])
    else:
        # If gdown is installed, let's update it to ensure we have the latest version
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'gdown'])

# Run the function to install or update gdown
install_or_update_gdown()

# Define your file IDs and desired output file names
file_ids = [
    '11BMwVZ8bEe0D0N49prtiEJNGZ3YEdbXQ', 
    '1FPj_tiITss5vJF91SrfPEURH6CUEmo4u', 
    '19-F30f-3IVj4q2R-fF6obfre1R42FlsX', 
    '16RRqOiNTxb-FbfH5HNZX1jI6LeVw15gT'
]
file_names = [
    'ViT_pretrain.ckpt', 
    'SegVol_v1.pth', 
    'Case_label_00001.nii.gz', 
    'Case_image_00001_0000.nii.gz'
]

# Define your save directory
save_directory = '/home/scur0402/SegVol/demo'
os.makedirs(save_directory, exist_ok=True)  # Ensure the directory exists

# Loop over the file IDs and names to download each one
for file_id, file_name in zip(file_ids, file_names):
    # Construct the full Google Drive download link
    file_url = f'https://drive.google.com/uc?id={file_id}'
    
    # Construct the full path to save the file
    output_path = os.path.join(save_directory, file_name)
    
    # Use gdown to download the file directly using the file ID
    gdown.download(id=file_id, output=output_path, quiet=False)
    print(f'{file_name} has been downloaded to {save_directory}.')
