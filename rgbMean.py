import imageInfo

class RgbMean:
    """
    Get mean RGB value

    :param image_path: Path to the image file.
    :type image_path: str
    :return: RGB values mean.
    :rtype: tuple(int, int, int)
    """
    def get_single_image_rgb_mean(rgb_matrix):
        r_sum = 0
        g_sum = 0
        b_sum = 0
        for rgb_set in rgb_matrix:
            r_sum += rgb_set[0]
            g_sum += rgb_set[1]
            b_sum += rgb_set[2]
        r_avg = r_sum // len(rgb_matrix)
        g_avg = g_sum // len(rgb_matrix)
        b_avg = b_sum // len(rgb_matrix)
        return [r_avg, g_avg, b_avg]
        
        
# import time
# rgbMean = RgbMean
# start = time.perf_counter()
# # rgb_mean = rgbMean.get_single_image_rgb_mean(imageInfo.ImageInfo.get_image_rgb_matrix("D:\PG\SEM 8\Data-preparation\merged-data\Healthy\8bc2979962db6549.jpg"))
# img = imageInfo.ImageInfo.get_image_rgb_matrix("D:\PG\SEM 8\Data-preparation\merged-data\Healthy\8bc2979962db6549.jpg")
# end = time.perf_counter()
# print(f"time = {end - start:0.4f}")
# # print(rgb_mean[0])