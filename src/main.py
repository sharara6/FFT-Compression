from image_utils import load_grayscale_image, show_images, save_compressed_image
from compression import compress_image
from metrics import analyze_compression_quality

def main():

    img = load_grayscale_image('img/ToBeCompressed.jpg')
    keep_percentage = 10    
    img_compressed = compress_image(img, keep_percentage)
    
    results = analyze_compression_quality(img, img_compressed, keep_percentage)
    
    print(f"PSNR: {results['psnr']:.2f} dB")
    print(f"SSIM: {results['ssim']:.4f}")
    print(f"Estimated Compression Ratio: {results['compression_ratio']:.1f}:1")
    
    show_images(img, img_compressed)
    
  
    save_compressed_image(img_compressed, 'img/compressed.jpg')

if __name__ == "__main__":
    main()