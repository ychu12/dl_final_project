# TODO:

1. Convert image data to pixel data, and put that in a csv file. Turns out, the labels are "A, B, E, G", where in the folders, patient IDs starting with 'A' were diagonosed with Adenocarcinoma, 'B' with Small Cell Carcinoma, 'E' with Large Cell Carcinoma, and 'G' with Squamous Cell Carcinoma.

2. Do something like an 80/20 split on the csv file for training and testing. Then, use that in the model and test different architectures. We're aiming for a maximum a posteriori probability (MAP) of around 0.87 on the validation set.

How the program works:
- The notebook file contains the model architecture logic
- The preprocess.py file is basically a preprocessing file that is called in the notebook.

Other Notes:
- The visualization code works when you pip install all the requirements, use "float" instead of np.float (depricated) in roi2rect.py, and when you run "pip install pascal-voc-tools".

Example usage:
"python preprocess.py --dicom-mode CT --dicom-path dl_data/images/Lung_Dx-A0001 --annotation-path dl_data/annotations/A0001 --classfile category.txt"
"python visualization.py --dicom-mode CT --dicom-path dl_data/images/Lung_Dx-A0001 --annotation-path dl_data/annotations/A0001 --classfile category.txt"