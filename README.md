# FFT-Compression

A Python-based image compression tool that uses Fast Fourier Transform (FFT) to reduce image file sizes while maintaining visual quality.

## Overview

This project implements frequency domain image compression using the Discrete Fourier Transform. It works by:

1. Converting an image to its frequency domain representation using FFT
2. Removing high-frequency components (which often represent fine details/noise)
3. Converting back to the spatial domain using inverse FFT

The result is a visually similar image with reduced data requirements.

## Project Structure

The project is divided into three main components:

- **Image Handling** (`image_utils.py`): Loading, displaying and saving image files
- **Compression Engine** (`compression.py`): Core FFT implementation and frequency filtering
- **Quality Metrics** (`metrics.py`): PSNR/SSIM calculation and compression ratio analysis

## Requirements

- Python 3.6+
- OpenCV (`cv2`)
- NumPy
- Matplotlib
- scikit-image

Install dependencies with:

```
pip install opencv-python numpy matplotlib scikit-image
```

## Usage

Place your image in the `img` directory, then run:

```
python src/main.py
```

By default, the program:

- Loads `img/ToBeCompressed.jpg`
- Compresses it by keeping only 10% of frequency components
- Displays original and compressed images side by side
- Saves the result as `img/compressed.jpg`
- Prints quality metrics (PSNR, SSIM, compression ratio)

## Customization

Modify `src/main.py` to:

- Change the input/output file paths
- Adjust the compression level (parameter `keep_percentage`)
- Enable/disable visualization

## Team

This project is structured for collaborative development with clear separation of concerns:

- **Image Handling**: Image I/O, visualization, format support
- **Compression Engine**: FFT algorithms, filtering methods, optimization
- **Quality Metrics**: Evaluation metrics, comparative analysis, benchmarking
