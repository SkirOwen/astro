import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import os

directory = "gaia-606"


all_images_offset = os.listdir(directory)

hdu_v = [fits.open(os.path.join(flat_v, images)) for images in all_images_name_v_list]
data_list_v = [images[0].data for images in hdu_v]

all_images_name_list = os.listdir(flat_r)

offset_lst_files = [os.path.join(directory, name) for name in all_images_name_list if "Offset" in name]
flat_lst_files = [os.path.join(directory, name) for name in all_images_name_list if "Flat" in name]
gaia_lst_files = [os.path.join(directory, name) for name in all_images_name_list if "Gaia" in name]


hdu_r = [fits.open(os.path.join(flat_r, images)) for images in all_images_name_r_list]
data_list_r = [images[0].data for images in hdu_r]

all_images_name_b_list = os.listdir(flat_b)

hdu_b = [fits.open(os.path.join(flat_b, images)) for images in all_images_name_b_list]
data_list_b = [images[0].data for images in hdu_b]

master_offset_v = np.mean(data_list_v, axis=0)