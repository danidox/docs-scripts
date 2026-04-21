import os
from PIL import Image
import sys

def convert_png_to_webp_and_overwrite(input_folder):
    for root, _, files in os.walk(input_folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_name, ext = os.path.splitext(file)

            if ext.lower() == ".png":
                webp_path = os.path.join(root, file_name + ".webp")
                try:
                    with Image.open(file_path) as img:
                        img.save(webp_path, "WEBP", quality=90)

                    # Remove the original .png file
                    os.remove(file_path)
                    print(f"✅ Converted and replaced: {file}")
                except Exception as e:
                    print(f"❌ Failed to convert {file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("⚠️ Usage: python webpmaker.py <folder_path>")
        sys.exit(1)

    folder = sys.argv[1]
    if os.path.isdir(folder):
        convert_png_to_webp_and_overwrite(folder)
        print("\n🎉 Conversion complete!")
    else:
        print("⚠️ Invalid folder path.")
