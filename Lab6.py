#Image Compression

from PIL import Image
import os
import matplotlib.pyplot as plt

def compress_image(input_path, output_path, quality=85):
    """Compress an image and save it with the specified quality."""
    with Image.open(input_path) as img:
        # Convert image to RGB mode if it's not already
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        img.save(output_path, 'JPEG', quality=quality, optimize=True)  # Save as JPEG with compression

def plot_images(original_path, compressed_path):
    """Plot the original image and compressed image side by side."""
    plt.subplot(1, 2, 1)
    plt.imshow(Image.open(original_path))
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(Image.open(compressed_path))
    plt.title('Compressed Image')

    plt.show()

def get_file_size(file_path):
    """Return the file size in bytes."""
    return os.path.getsize(file_path)

def main():
    # Define file paths
    input_image_path = '/Users/bipinsaud/Desktop/texas.png'  # Replace with your image file
    output_image_path = '/Users/bipinsaud/Desktop/Ctexas.png'

    # Set compression quality (0-100, higher is better quality)
    compression_quality = 85

    # Compress image
    compress_image(input_image_path, output_image_path, quality=compression_quality)

    # Get and display file sizes
    original_size = get_file_size(input_image_path)
    compressed_size = get_file_size(output_image_path)
    print(f'Original Image Size: {original_size} bytes')
    print(f'Compressed Image Size: {compressed_size} bytes')

    # Plot the images
    plot_images(input_image_path, output_image_path)

if __name__ == "__main__":
    main()
