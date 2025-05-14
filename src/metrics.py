from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim


def compute_metrics(original, compressed):

    psnr_value = psnr(original, compressed)
    ssim_value = ssim(original, compressed)
    return psnr_value, ssim_value


def compute_compression_ratio(keep_percentage):

    return 100 / keep_percentage


def analyze_compression_quality(original, compressed, keep_percentage):

    psnr_val, ssim_val = compute_metrics(original, compressed)
    comp_ratio = compute_compression_ratio(keep_percentage)

    results = {
        "psnr": psnr_val,
        "ssim": ssim_val,
        "compression_ratio": comp_ratio,
        "kept_frequencies": keep_percentage
    }

    return results
