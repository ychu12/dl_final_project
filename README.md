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
- When the image target shape is (256,256) as opposed to the default (512,512) without reshaping/compressing the images, the model takes like 3-5 minutes to run and eventually reaches 100% training accuracy. When compressed to (128,128), it runs much faster, but only gets up to ~92% training accuracy, which is less sus imo.
- MLP runs super quick, but the validation loss is super high.

TODO:
1. Use more data. Right now, the accuracy is 100%, which is kinda sus. It makes sense, however, because at the moment, only "A" labels are being used.
^Update to the first TODO: Validation accuracy now ~85% with image resizing to (128,128). Maybe run again to check if it's legit.
2. Try out different architectures (such as an MLP).
3. Make it so that in the preprocessing, "output.csv" is overwritten, so that I don't have to keep deleting it before every run.
- Whatever else is in the handout/brief.
- Maybe email the TA when we're done and ask what he thinks.