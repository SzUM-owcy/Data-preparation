import PIL.Image

class ImageInfo:
    @staticmethod
    def get_image_info(image_path):
        img = PIL.Image.open(image_path)
        info = img.getexif()
        print(info)
        
ImageInfo.get_image_info("d:\PG\SEM 8\Train\Healthy\8bc2979962db6549.jpg")