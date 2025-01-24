import cv2
from cams_ilvo_utils.img.image import unsquare, Image
import numpy as np
import torch
from copy import deepcopy
from skimage.feature import peak_local_max
from centernet_ilvo.center import Center, CenterList


def hm_out_abs(cv_hm):
    """
    Converts weight output (cv_hm) to a hm with only positive values
    """
    return np.add(np.ones(cv_hm.shape) * abs(np.min(cv_hm)), cv_hm)


def hm_out_to_cv_im(cv_hm, orig_size):
    """
    Converts weight output (cv_hm) to an opencv image with the original size
    """
    orig_h_px, orig_w_px = orig_size

    hm_im = cv2.resize(cv_hm, (orig_h_px, orig_h_px), None, None, None, cv2.INTER_LINEAR)
    if orig_w_px != orig_h_px:
        hm_im = unsquare(hm_im, orig_w_px)

    return hm_im


def hm_in_to_cv_im(im_hm: Image, new_size=None):
    """
    Converts weight input (im_hm) to an opencv image with the new size
    """
    cv_im = deepcopy(im_hm.get())
    if new_size:
        cv2.resize(cv_im, new_size, cv_im)
    cv_im = cv2.normalize(cv_im, None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    cv_im = cv_im.transpose([2, 0, 1])
    return cv_im


def predict_center(model, device, im_input=(np.ndarray,Image), scale=20, orig_size=None):
    """
    Predicts the weight output for input_im
    """
    if isinstance(im_input, np.ndarray):
        im_input = Image(im_input)

    im_input.square().set(cv2.resize(im_input.get(), (512, 512)))
    cv_im_input = hm_in_to_cv_im(im_input)

    # Save original image size
    if orig_size is None:
        orig_size = cv_im_input.shape[1:3]

    # Push the image through the weight
    img = torch.from_numpy(cv_im_input)
    with torch.no_grad():
        hm_tensor = model(img.to(device).float().unsqueeze(0))

    hm_out = hm_tensor.cpu().numpy().squeeze(0).squeeze(0)

    s_new = hm_out.shape[0]
    h_orig, w_orig = orig_size

    # resize the output
    # * image
    hm_abs = hm_out_abs(hm_out * scale)
    centers_px = peak_local_max(hm_abs.astype(float), threshold_abs=50, num_peaks=1)
    cv_hm = hm_out_to_cv_im(hm_abs, orig_size)
    # * centers
    offset_x = int((w_orig - h_orig) / 2)

    # create a centers list
    centers = CenterList()
    for center_px in centers_px:
        centers.append(
            Center(center_px=(offset_x + int(center_px[1] * (h_orig / s_new)), int(center_px[0] * (h_orig / s_new))),
                   cv_image=cv_hm))

    return cv_hm, centers
