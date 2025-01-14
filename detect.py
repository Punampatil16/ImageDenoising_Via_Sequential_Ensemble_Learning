import cv2
from skimage import io, img_as_ubyte, img_as_float, color  
from skimage.restoration import denoise_nl_means
from skimage.filters import gaussian
from pywt import wavedec2, waverec2
import os

# Read the image 
filepath = "C:\\Users\\Soham\\Desktop\\IMG denoise\\noisy.jpg"
cv2.imwrite("C:\\Users\\Soham\\Desktop\\IMG denoise\\noisy1.jpg", filepath)
img = io.imread(filepath)  

# Convert the image to float32 and resize
img_float32 = cv2.resize(img_as_float(img), (350, 350)) 

# Convert the image to 8-bit unsigned integers (CV_8U)
img_uint8 = img_as_ubyte(img_float32)

# Check if the image is grayscale and convert to color if necessary
if len(img_float32.shape) == 2:  
    img_uint8 = cv2.cvtColor(img_uint8, cv2.COLOR_GRAY2RGB)

# Split the image into channels if it's a color image
if len(img_uint8.shape) == 3 and img_uint8.shape[2] == 3:
    R_channel, G_channel, B_channel = cv2.split(img_uint8)

    # Denoise each channel separately
    denoise_nl_means_R = denoise_nl_means(R_channel, h=0.1, sigma=0.02, patch_size=5, patch_distance=6)
    denoise_nl_means_G = denoise_nl_means(G_channel, h=0.1, sigma=0.02, patch_size=5, patch_distance=6)
    denoise_nl_means_B = denoise_nl_means(B_channel, h=0.1, sigma=0.02, patch_size=5, patch_distance=6)

    # Combine the denoised channels back into a single color image
    denoised_color_img_uint8 = cv2.merge([denoise_nl_means_R, denoise_nl_means_G, denoise_nl_means_B])

    # Convert the denoised color image to the appropriate data type for saving
    denoised_color_img_uint8 = img_as_ubyte(denoised_color_img_uint8)

    # Save the denoised color image
    cv2.imwrite("C:\\Users\\Soham\\Desktop\\IMG denoise\\noisy1.jpg", cv2.cvtColor(denoised_color_img_uint8, cv2.COLOR_BGR2RGB))

else:  
    # Apply denoising algorithms to the grayscale image
    def denoise_gaussian(image):
        return gaussian(image, sigma=1)

    def denoise_cv2_gaussian(image):
        return cv2.GaussianBlur(image, (3, 3), 0)

    def denoise_wavelet(image):
        coeffs = wavedec2(image, 'haar', level=1, axes=(0, 1))
        sigma = 0.1  
        detail_coeffs_scaled = [tuple(sigma * c for c in coef) for coef in coeffs[1:]]  
        new_coeffs = [coeffs[0]] + detail_coeffs_scaled  
        denoised_img = waverec2(new_coeffs, 'haar', axes=(0, 1))
        return denoised_img

    # Apply denoising algorithms to the grayscale image
    gray_img_float32_resized = cv2.resize(img_as_float(color.rgb2gray(img_uint8)), (320, 480))  

    denoise_gaussian_gray = denoise_gaussian(gray_img_float32_resized)
    denoise_cv2_gaussian_gray = denoise_cv2_gaussian(gray_img_float32_resized)
    denoise_wavelet_gray = denoise_wavelet(gray_img_float32_resized)

    # Combine results for the grayscale image
    ensemble_gray = (denoise_gaussian_gray + denoise_cv2_gaussian_gray + denoise_wavelet_gray) / 3

    # Convert the ensemble grayscale image to the appropriate data type for saving
    ensemble_gray_uint8 = img_as_ubyte(ensemble_gray)

    # Save the denoised grayscale image
    cv2.imwrite("C:\\Users\\Soham\\Desktop\\IMG denoise\\noisy1.jpg", ensemble_gray_uint8)

print("Images saved successfully.")
