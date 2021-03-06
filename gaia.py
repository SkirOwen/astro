import numpy as np
from astropy.io import fits
# import matplotlib.pyplot as plt
import os
import time

directory = "gaia-606"
output_dir = "CORRECTED_gaia-606"

all_images_name_list = os.listdir(directory)

offset_lst_files = [os.path.join(directory, name) for name in all_images_name_list if "Offset" in name]
flat_lst_files = [os.path.join(directory, name) for name in all_images_name_list if "Flat" in name]
gaia_lst_files = [os.path.join(directory, name) for name in all_images_name_list if "Gaia" in name]

# offset
hdu_offset = [fits.open(images) for images in offset_lst_files]
data_list_offset = [images[0].data for images in hdu_offset]
master_offset = np.median(data_list_offset, axis=0)

# flat
hdu_flat = [fits.open(images) for images in flat_lst_files]
data_list_flat = [images[0].data for images in hdu_flat]
master_flat = np.median(data_list_flat, axis=0)


def flat_field(images_index):
    global master_flat
    global master_offset

    im = fits.open(gaia_lst_files[images_index])
    data_im = im[0].data
    data_im_new = ((data_im - master_offset) * np.mean(master_flat)) / (master_flat - master_offset)
    name = ("image_corrected_" + str(images_index+1).zfill(3) + ".fits")
    fits.writeto(os.path.join(output_dir, name), data_im_new, im[0].header)
    print("image_corrected_" + str(images_index+1).zfill(3) + ".fits" + " has been created")
    return


if __name__ == "__main__":
    start_time = time.time()
    for i in range(len(gaia_lst_files)):
        flat_field(i)
    end_time = time.time()
    print("Completed in: ", (end_time - start_time))

# data_im_new, im = flat_field(0)
#
# fits.writeto("test.fits", data_im_new, im[0].header)
# fits.writeto("test_flat.fits", master_flat, im[0].header)
