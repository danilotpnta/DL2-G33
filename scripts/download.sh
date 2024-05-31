save_folder=$(pwd)/datasets

if [ ! -d $save_folder ]; then
    GIT_LFS_SKIP_SMUDGE=1 git submodule update --init --recursive
fi

# Dataset should follow the format of 0000-0018
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <dataset_number>"
    exit 1
fi

if [[ $1 != "24_1" && $1 != "24_2" && ($1 -lt 0 || $1 -gt 23) ]]; then
    echo "Dataset number should be between 0 and 24(_1, _2)."
    exit 1
fi


if [[ $1 == "24_1" ]] || [[ $1 == "24_2" ]]; then
    dataset="00$1"
else
    dataset=$(printf "%04d" $1)
fi

cd "$save_folder/M3D_Seg"
if [ ! -f $save_folder/$dataset ]; then
    echo "Downloading $dataset ..."
    git lfs pull --include="$dataset.zip"
    echo "Unzipping $dataset ..."
    unzip $save_folder/M3D_Seg/$dataset
    echo "Done!"
else
    echo "$dataset already exists."
fi