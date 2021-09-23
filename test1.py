from skimage.metrics import structural_similarity as compare_ssim
from skimage.io import imread
from skimage.color import rgb2gray

ref_image = imread('11.png')
ref_image = rgb2gray(ref_image)
impaired_image = imread('New.png')
impaired_image = rgb2gray(impaired_image)

score = compare_ssim(ref_image, impaired_image, multichannel=True, gaussian_weights=True, sigma=1.5, use_sample_covariance=False, data_range=1.0)

print(score)
