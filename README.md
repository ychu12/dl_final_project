# TODO:

How the program works:
- The notebook file contains the model architecture logic
- The preprocess.py file is basically a preprocessing file that is called in the notebook.

Example usage:
"python preprocess.py --dicom-mode CT --dicom-path dl_data/images/Lung_Dx-A0001 --annotation-path dl_data/annotations/A0001 --classfile category.txt"
"python visualization.py --dicom-mode CT --dicom-path dl_data/images/Lung_Dx-A0001 --annotation-path dl_data/annotations/A0001 --classfile category.txt"

Other Notes:
- The visualization code works when you pip install all the requirements, use "float" instead of np.float (depricated) in roi2rect.py, and when you run "pip install pascal-voc-tools".
- So far, only CT scan images are being processed because only the default argument for --dicom-mode is being used (the argument is "CT").
- We're aiming for a maximum a posteriori probability (MAP) of around 0.87 on the validation set.
- Overall, the model actually predicts type of cancer from images, rather than if there is cancer in an image.

Major things done so far:
- Converted image data to pixel data, and put that into a csv file. The labels are "A, B, E, G", where in the folders, patient IDs starting with 'A' were diagonosed with Adenocarcinoma, 'B' with Small Cell Carcinoma, 'E' with Large Cell Carcinoma, and 'G' with Squamous Cell Carcinoma.
- Constructed the model and ran it

TODO:
- Use more data. Right now, the accuracy is 100%, which is kinda sus. It makes sense, however, because at the moment, only "A" labels are being used.