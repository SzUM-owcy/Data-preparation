import imageInfo
import os
import multiprocessing
import matplotlib.pyplot as plt
import seaborn as sns

class RgbMean:
    """
    Get mean RGB value

    :param rgb_matrix: RGB matrix of image.
    :type rgb_matrix: 
    :return: RGB values mean.
    :rtype: tuple(int, int, int)
    """
    def get_rgb_matrix_mean(self, rgb_matrix):
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
    
    
    def get_single_image_rgb_mean(self, file_path):
        rgb_matrix = imageInfo.ImageInfo.get_image_rgb_matrix(file_path)
        return self.get_rgb_matrix_mean(rgb_matrix)
    
    """
    Get count of specific RGB colour

    :param rgb_means: array that contains RGB means for images.
    :type [[avg_R1, avg_G1, avg_B1], [avg_R2, avg_G2, avg_B2]...]: 
    :return: count of specific RGB values.
    :rtype: array[
        [
            [0:count],
            [1:count],
            [255:count]
        ] # FOR Red,
        [...] # FOR Green,
        [...] # FOR Blue
    ]
    """
    def get_rgb_count(self, rgb_means):
        MIN_RGB_VALUE = 0
        MAX_RGB_VALUE = 255
        R_count = [0 for rgb_value in range(MIN_RGB_VALUE, MAX_RGB_VALUE + 1)]
        G_count = [0 for rgb_value in range(MIN_RGB_VALUE, MAX_RGB_VALUE + 1)]
        B_count = [0 for rgb_value in range(MIN_RGB_VALUE, MAX_RGB_VALUE + 1)]
        for rgb_mean in rgb_means:
            R_count[rgb_mean[0]] += 1
            G_count[rgb_mean[1]] += 1
            B_count[rgb_mean[2]] += 1
        return [R_count, G_count, B_count]            