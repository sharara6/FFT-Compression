import numpy as np


def apply_fft(img):

    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    return fshift


def filter_frequencies(fshift, keep_percentage=10):

    rows, cols = fshift.shape
    crow, ccol = rows // 2, cols // 2

    mask = np.zeros((rows, cols), np.uint8)
    r_keep = int(rows * keep_percentage / 100 / 2)
    c_keep = int(cols * keep_percentage / 100 / 2)
    mask[crow - r_keep:crow + r_keep, ccol - c_keep:ccol + c_keep] = 1

    fshift_filtered = fshift * mask
    return fshift_filtered


def apply_ifft(fshift_filtered):

    f_ishift = np.fft.ifftshift(fshift_filtered)
    img_reconstructed = np.fft.ifft2(f_ishift)
    img_reconstructed = np.abs(img_reconstructed)
    return np.uint8(np.clip(img_reconstructed, 0, 255))


def compress_image(img, keep_percentage=10):

    fshift = apply_fft(img)
    fshift_filtered = filter_frequencies(fshift, keep_percentage)
    img_compressed = apply_ifft(fshift_filtered)
    return img_compressed
