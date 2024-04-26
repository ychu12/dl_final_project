import argparse
import os
from getUID import getUID_path, loadFile
from get_gt import get_gt
#from roi2rect import roi2rect, MatrixToImage, PETToImage
from get_data_from_XML import XML_preprocessor, get_category
import pydicom
import pandas as pd

def dcm_to_csv(dcm_path, dcm_name, has_annotations, csv_path):
    # We're assuming that if has_annotations = 1, then there 
    # is cancer. If it's 0, then there's no cancer.
    ds = pydicom.dcmread(dcm_path)
    pixel_array = ds.pixel_array

    # Flatten the array to 1D and convert to string format
    flat_pixels = pixel_array.flatten()
    pixel_strings = " ".join(map(str, flat_pixels))

    data_to_append = {'File Name': dcm_name, 'Pixel Data': pixel_strings, 'Has Annotations': has_annotations}

    # Check if CSV exists and append data
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        new_df = pd.DataFrame([data_to_append])
        updated_df = pd.concat([df, new_df], ignore_index=True)
        updated_df.to_csv(csv_path, index=False)
    else:
        df = pd.DataFrame([data_to_append])
        df.to_csv(csv_path, index=False)

# Functions below from the stencil given by the site with the image data
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
    main_dict = getUID_path(args.dicom_path)
    csv_path = 'output.csv'

    if os.path.isdir(args.annotation_path):
        annotations = XML_preprocessor(args.annotation_path, num_classes=num_classes).data
        print(annotations.items())
        for k, v in annotations.items():
            dcm_path, dcm_name = main_dict[k[:-4]]
            # image_data = v
            dcm_to_csv(dcm_path, dcm_name, 1, csv_path)

            # if args.dicom_mode == 'CT':
            #     matrix, frame_num, width, height, ch = loadFile(os.path.join(dcm_path))
            #     print(dcm_path)
            # elif args.dicom_mode == 'PET':
            #     img_array, frame_num, width, height, ch = loadFile(dcm_path)


if __name__ == '__main__':
    #main("CT", "dl_data/images", "dl_data/annotations", "category.txt")
    main()
