import argparse
import os
from getUID import getUID_path, loadFile
from get_gt import get_gt
#from roi2rect import roi2rect, MatrixToImage, PETToImage
from get_data_from_XML import XML_preprocessor, get_category


# Some of the stencil code uses depricated code, but it is still needed
# These two lines clean up the terminal outputs
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


import pydicom
import pandas as pd
import numpy as np
from skimage.transform import resize

def resize_image(pixel_array, target_size):
    resized_image = resize(pixel_array, target_size, mode='constant', anti_aliasing=True, preserve_range=True)

    return resized_image

def dcm_to_csv(dcm_path, dcm_name, csv_path, cancer_type):
    ds = pydicom.dcmread(dcm_path)
    pixel_array = ds.pixel_array

    # Raw target_size is (512,512). Comment the below line out to use the raw target size
    pixel_array = resize_image(pixel_array, target_size=(64, 64))

    # Flatten the pixel array to 1D and convert to string format
    flat_pixels = pixel_array.flatten()
    pixel_strings = " ".join(map(str, flat_pixels))

    data_to_append = {'file_name': dcm_name, 'pixel_data': pixel_strings, 'cancer_type': cancer_type}

    # Check if CSV exists and append data
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        new_df = pd.DataFrame([data_to_append])
        updated_df = pd.concat([df, new_df], ignore_index=True)
        updated_df.to_csv(csv_path, index=False)
    else:
        df = pd.DataFrame([data_to_append])
        df.to_csv(csv_path, index=False)

# Modified functions below from the stencil given by the site with the image data
def parse_args():
    parser = argparse.ArgumentParser('Annotation Visualization')
    parser.add_argument('--dicom-mode', type=str, default='CT', choices=['CT', 'PET'])
    parser.add_argument('--dicom-path', type=str, help='path to the folder storing DICOM files (.DCM)')
    parser.add_argument('--annotation-path', type=str, help='path to the folder storing annotation files (.xml)')
    parser.add_argument('--classfile', type=str, default='category.txt', help='path to the text file storing categories')
    return parser.parse_args()

def main():
    args = parse_args()
    class_list = get_category(args.classfile)
    num_classes = len(class_list)
    try:
        main_dict = getUID_path(args.dicom_path)
        print("Folder/File Found")
    except: 
        # print("Probably FileNotFound error")
        exit(1) # Kill the program, effectively breaking out of the loop.

    csv_path = 'output.csv'

    if os.path.isdir(args.annotation_path):
        patient_id = args.annotation_path.split("s/", 1)[-1]
        annotations = XML_preprocessor(args.annotation_path, num_classes=num_classes).data
        for k, v in annotations.items():
            try:
                dcm_path, dcm_name = main_dict[k[:-4]]
            except:
                print("Possible key error")    
                continue
            # image_data = v
            dcm_to_csv(dcm_path, dcm_name, csv_path, patient_id[0])

if __name__ == '__main__': 
    main()
