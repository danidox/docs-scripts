#!/usr/bin/env python3
import os
import sys
from PIL import Image

def convert_images_to_webp(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        sys.exit(1)

    # Create output directory
    output_dir = os.path.join(folder_path, "webp_converted")
    os.makedirs(output_dir, exist_ok=True)

    supported_extensions = ('.jpg', '.jpeg', '.png')
    converted_count = 0

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(supported_extensions):
            input_path = os.path.join(folder_path, filename)
            output_filename = os.path.splitext(filename)[0] + ".webp"
            output_path = os.path.join(output_dir, output_filename)

            try:
                with Image.open(input_path) as img:
                    img.save(output_path, "WEBP")
                print(f"Converted: {filename} → {output_filename}")
                converted_count += 1
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

    print(f"\nConversion complete. {converted_count} image(s) saved in '{output_dir}'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_to_webp.py <image_folder>")
        sys.exit(1)

    folder = sys.argv[1]
    convert_images_to_webp(folder)
