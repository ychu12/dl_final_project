import argparse
import os
from getUID import getUID_path, loadFile
from get_gt import get_gt
#from roi2rect import roi2rect, MatrixToImage, PETToImage
from get_data_from_XML import XML_preprocessor, get_category

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

    if os.path.isdir(args.annotation_path):
        annotations = XML_preprocessor(args.annotation_path, num_classes=num_classes).data
        for k, v in annotations.items():
            dcm_path, dcm_name = main_dict[k[:-4]]
            image_data = v

            if args.dicom_mode == 'CT':
                matrix, frame_num, width, height, ch = loadFile(os.path.join(dcm_path))
                print(dcm_path)
            elif args.dicom_mode == 'PET':
                img_array, frame_num, width, height, ch = loadFile(dcm_path)


if __name__ == '__main__':
    #main("CT", "dl_data/images", "dl_data/annotations", "category.txt")
    main()
