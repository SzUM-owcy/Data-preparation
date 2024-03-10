from PIL import Image, ExitTags
import PIL

class ImageInfo:
    @staticmethod
    def get_image_info(image_path):
        img = PIL.Image.open(image_path)
        info = img.getexif()
        if info is None:
            print('Sorry, image has no exif data.')
        else:
            for key, val in info.items():
                print(f'{key}:{val}')
        
ImageInfo.get_image_info("d:\PG\SEM 8\Train\Healthy\8bc2979962db6549.jpg")