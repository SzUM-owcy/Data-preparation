from PIL import Image

class ImageInfo:
    @staticmethod
    def get_image_size(image_path):
        try:
            img = Image.open(image_path)
            width, height = img.size
            return width, height
            
        except Exception as ex:
            print("ImageInfo error: ", ex)
            
    @staticmethod
    def get_image_rgb_matrix(image_path):
        try:
            img = Image.open(image_path)
            rgb_matrix = list(img.getdata())
            return rgb_matrix
            
        except Exception as ex:
            print("ImageInfo error: ", ex)
