import matplotlib.pyplot as plt
import numpy as np
from helper import load_image


def get_segment(bounds_array, original_img):
    segmented_image = np.zeros([original_img.size[1], original_img.size[0], 3], dtype=np.uint8)
    for i in range(bounds_array.shape[0]):
        for j in range(bounds_array.shape[1]):
            if bounds_array[i][j] == 0:
                segmented_image[i][j] = [255, 255, 255]
            else:
                segmented_image[i][j] = [0, 0, 0]
    return segmented_image


def show_segment(image_name='2092'):
    ground_truth, img = load_image(image_name)
    img.show()
    for i in range(ground_truth.shape[1]):
        segment = ground_truth[0, i]
        bound = segment[0, 0][1]
        segmented_image = get_segment(bound, img)
        plt.figure(i + 1)
        plt.imshow(segmented_image)
    plt.show()

show_segment('183087')
