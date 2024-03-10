from PIL import Image

class ImageInfo:
    
    @staticmethod
    def get_image_size(image_path):
        """
        Get the width and height of the image.

        :param image_path: Path to the image file.
        :type image_path: str
        :return: Width and height of the image.
        :rtype: tuple(int, int)
        """
        try:
            img = Image.open(image_path)
            width, height = img.size
            return width, height
            
        except Exception as ex:
            print("ImageInfo error: ", ex)
            
    @staticmethod
    def get_image_rgb_matrix(image_path):
        """
        Get the RGB color matrix of the image.

        :param image_path: Path to the image file.
        :type image_path: str
        :return: RGB color matrix of the image.
        :rtype: list(tuple(int, int, int))
        """
        try:
            img = Image.open(image_path)
            rgb_matrix = list(img.getdata())
            return rgb_matrix
            
        except Exception as ex:
            print("ImageInfo error: ", ex)
