from PIL import Image

# simple image processing -> convert other format to png


def convert_tif_to_png(tif_path, png_path):
    try:
        with Image.open(tif_path) as im:
            # Ensure image mode is compatible with PNG (e.g., convert to RGBA if necessary)
            if im.mode not in ('RGB', 'RGBA', 'L', 'P'):
                im = im.convert('RGBA')
            im.save(png_path, 'PNG')
        print(f"Successfully converted: {tif_path} to {png_path}")
    except IOError as e:
        print(f"Error converting file {tif_path}: {e}")

path_img1 = "data\\img\\1.tiff"
convert_tif_to_png(path_img1, path_img1.replace(".tiff",".png").replace(".tif",".png"))

# =============================================================================
# =============================================================================

def convert_bmp_to_png(bmp_path, png_path):
    try:
        # Open the image file
        with Image.open(bmp_path) as img:
            # Save the image with the new PNG format
            img.save(png_path, 'PNG')
        print(f"Successfully converted {bmp_path} to {png_path}")
    except IOError as e:
        print(f"Error converting image: {e}")


path_img2 = "data\\img\\2.bmp"
convert_bmp_to_png(path_img2, path_img2.replace(".bmp",".png"))
