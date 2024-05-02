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
- Overall, the model actually predicts type of cancer from images, rather than if there is cancer in an image.

TODO:
- Yen needs to communicate the results of the model (Yen wrote this lmao)
- Perhaps LIME stuff (Brian)
- Whatever else is in the handout/brief (ex: Poster)

Some analysis:
- The MLP model runs really quickly (5 seconds), and seems to have reasonable results after 20 epochs. The CNN model takes much longer to run, and seems to overfit, no matter what I try to do to fix it (BatchNorm, Dropout, L2 regularization, decreasing the learning rate and number of neurons/layers).
- A stratified train/test split is used on the ~2.66 gigs of image data to ensure equal representation. The image sizes are resized from (512, 512) -> (128,128) to help with model performance (mainly for the CNN, the MLP is fine).

Max's questions (Yen's answers):
1. We feel like the project has turned out well. We were able to attempt some stretch goals (trying out different architectures such as the CNN), and we reached our target and base goals (implementing a working MLP model).
2. The MLP works the way we expected, with reasonable training and validation losses, and reasonable training and validation accuracies after 20-30 epochs.
3. The CNN initally didn't work as intended, so we pivoted to implementing an MLP, which ran much faster and was easier to understand and implement. If we were to do this project differently, we would have read the data documentation earlier to make debugging easier.
4. If we had more time, we would improve the project by using all 100+ gigs of data rather than just 2.66 gigs of data.
5. We learned about working with real-world data and stencil code, as well as implementing DL models and tuning those models.