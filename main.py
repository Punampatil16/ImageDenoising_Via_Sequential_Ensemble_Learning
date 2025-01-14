# from tkinter import *
# from tkinter import filedialog
# from PIL import Image,ImageTk 
# import os 
# import shutil
# import cv2
# from skimage import io, img_as_ubyte, img_as_float, color  
# from skimage.restoration import denoise_nl_means
# from skimage.filters import gaussian
# from pywt import wavedec2, waverec2

# win = Tk()

# def copy_image(input_path, output_path):
#     try:
#         # Check if the input file exists
#         if not os.path.exists(input_path):
#             print("Input file does not exist.")
#             return
        
#         # Check if the output directory exists, if not, create it
#         output_dir = os.path.dirname(output_path)
#         if not os.path.exists(output_dir):
#             os.makedirs(output_dir)
        
#         # Copy the image file
        
#         print("Image copied successfully.")
#         return shutil.copy2(input_path, output_path)
        
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")

# def copy_image_result(input_path, output_path):
#     try:
#         # Check if the input file exists
#         if not os.path.exists(input_path):
#             print("Input file does not exist.")
#             return
        
#         # Check if the output directory exists, if not, create it
#         output_dir = os.path.dirname(output_path)
#         if not os.path.exists(output_dir):
#             os.makedirs(output_dir)
        
#         # Copy the image file
#         shutil.copy2(input_path, output_path)
#         print("Image copied successfully.")
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")

# def download():
#     file = open('basename.txt','r')
#     basename = file.read()
#     input_path = "C:/Users/COMP/Desktop/IMG denoise/result" + '/' +basename
#     output_path = "C:/Users/COMP/Downloads/"
#     try:
#         # Check if the input file exists
#         if not os.path.exists(input_path):
#             print("Input file does not exist.")
#             return
        
#         # Check if the output directory exists, if not, create it
#         output_dir = os.path.dirname(output_path)
#         if not os.path.exists(output_dir):
#             os.makedirs(output_dir)
        
#         # Copy the image file
#         shutil.copy2(input_path, output_path)
#         print("Image copied successfully.")
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")


# file_path =""
# win.state("zoomed")
# win.title("IMAGE DENOISING")
# win.config(bg="lightblue",)

# # Add a background image
# bg_image_path = bg_image_path = "C:\\Users\\COMP\\Pictures\\you-and-me-stargazing-zw.jpg"  # Replace with your background image path
# bg_image = Image.open(bg_image_path)
# bg_image = bg_image.resize((win.winfo_screenwidth(), win.winfo_screenheight()), Image.LANCZOS)
# bg_photo = ImageTk.PhotoImage(bg_image)


# l1 = Label(text="IMAGE DENOISING",font=("Bernard MT Condensed", 20 ), bg="black",fg= "white")
# l1.place(x=690,y=30)

# l4 = Label(text="→ REMOVE THE NOISE FROM IMAGE IN ONE CLICK",font=("Engravers MT", 20 ), bg="black",fg= "white")
# l4.place(x=365,y=125)



# def denoise():
#     filepath = "C:/Users/COMP/Desktop/IMG denoise/result"
    
#     file = open('basename.txt','r')
#     basename = file.read()
    
#     filepath = filepath + "/" + basename
#     # cv2.imwrite(filepath, filepath)
#     img = io.imread(filepath)  

#     # Convert the image to float32 and resize
#     img_float32 = cv2.resize(img_as_float(img), (350, 350)) 

#     # Convert the image to 8-bit unsigned integers (CV_8U)
#     img_uint8 = img_as_ubyte(img_float32)

#     # Check if the image is grayscale and convert to color if necessary
#     if len(img_float32.shape) == 2:  
#         img_uint8 = cv2.cvtColor(img_uint8, cv2.COLOR_GRAY2RGB)

#     # Split the image into channels if it's a color image
#     if len(img_uint8.shape) == 3 and img_uint8.shape[2] == 3:
#         R_channel, G_channel, B_channel = cv2.split(img_uint8)

#         # Denoise each channel separately
#         denoise_nl_means_R = denoise_nl_means(R_channel, h=0.1, sigma=0.02, patch_size=5, patch_distance=6)
#         denoise_nl_means_G = denoise_nl_means(G_channel, h=0.1, sigma=0.02, patch_size=5, patch_distance=6)
#         denoise_nl_means_B = denoise_nl_means(B_channel, h=0.1, sigma=0.02, patch_size=5, patch_distance=6)

#         # Combine the denoised channels back into a single color image
#         denoised_color_img_uint8 = cv2.merge([denoise_nl_means_R, denoise_nl_means_G, denoise_nl_means_B])

#         # Convert the denoised color image to the appropriate data type for saving
#         denoised_color_img_uint8 = img_as_ubyte(denoised_color_img_uint8)

#         # Save the denoised color image
#         cv2.imwrite(filepath, cv2.cvtColor(denoised_color_img_uint8, cv2.COLOR_BGR2RGB))

#     else:  
#         # Apply denoising algorithms to the grayscale image
#         def denoise_gaussian(image):
#             return gaussian(image, sigma=1)

#         def denoise_cv2_gaussian(image):
#             return cv2.GaussianBlur(image, (3, 3), 0)

#         def denoise_wavelet(image):
#             coeffs = wavedec2(image, 'haar', level=1, axes=(0, 1))
#             sigma = 0.1  
#             detail_coeffs_scaled = [tuple(sigma * c for c in coef) for coef in coeffs[1:]]  
#             new_coeffs = [coeffs[0]] + detail_coeffs_scaled  
#             denoised_img = waverec2(new_coeffs, 'haar', axes=(0, 1))
#             return denoised_img

#         # Apply denoising algorithms to the grayscale image
#         gray_img_float32_resized = cv2.resize(img_as_float(color.rgb2gray(img_uint8)), (320, 480))  

#         denoise_gaussian_gray = denoise_gaussian(gray_img_float32_resized)
#         denoise_cv2_gaussian_gray = denoise_cv2_gaussian(gray_img_float32_resized)
#         denoise_wavelet_gray = denoise_wavelet(gray_img_float32_resized)

#         # Combine results for the grayscale image
#         ensemble_gray = (denoise_gaussian_gray + denoise_cv2_gaussian_gray + denoise_wavelet_gray) / 3

#         # Convert the ensemble grayscale image to the appropriate data type for saving
#         ensemble_gray_uint8 = img_as_ubyte(ensemble_gray)

#         # Save the denoised grayscale image
#         cv2.imwrite(filepath, ensemble_gray_uint8)

#         print("Images saved successfully.")
#     original_image = Image.open(filepath)

#                     # Resize the image
#     resized_image = original_image.resize((500, 400), Image.LANCZOS)

#             # Create a PhotoImage object from the resized image
#     img1 = ImageTk.PhotoImage(resized_image)

#             # Create a label and set the image attribute
#     label1img = Label(f1, image=img1, bg='white')

#     label1img.image = img1  # Keep a reference to prevent garbage collection
#     label1img.place(x= 900,y=300)
    
#     downloadbtn = Button(win,text="Download", font=",20", bg="white", fg="black", command=download)
#     downloadbtn.place(x=750,y=700)

    
# def importimg():
#       file_path = filedialog.askopenfilename(title="Select Input Image File" , filetypes=[("Image files", "*.jpg;*.jpeg;*.png;")])
#       basename = os.path.basename(file_path)
#     #   print(basename)
      
#       basefile = open('basename.txt','w')


#       basefile.write(str(basename))
#       basefile.close()

#       copy_image(file_path,"C:\\Users\\COMP\\Desktop\\IMG denoise\\userdata" )
#       copy_image_result(file_path, "C:\\Users\\COMP\\Desktop\\IMG denoise\\result")
#       if(file_path):
#           denoisbtn = Button(win,text="denoise", font=",20", bg="white", fg="black", command=denoise)
#           denoisbtn.place(x=750,y=400)
          
         

#           path = file_path
#           original_image = Image.open(path)

#                     # Resize the image
#           resized_image = original_image.resize((500, 400), Image.LANCZOS)

#                     # Create a PhotoImage object from the resized image
#           img1 = ImageTk.PhotoImage(resized_image)

#                     # Create a label and set the image attribute
#           label1img = Label(f1, image=img1, bg='white')

#           label1img.image = img1  # Keep a reference to prevent garbage collection
#           label1img.place(x= 200,y=300)

# btn = Button(win,text="IMPORT IMAGE", font=",19", bg="LIGHTGREEN", fg="black", command=importimg)
# btn.place(x=720,y=70)

# l2 = Label(text="INPUT IMAGE",font=("Bodoni Bd BT", 20) , bg="black",fg= "white")
# l2.place(x=200,y=260)

# f1 = Frame(win,height=400,width=500).place(x= 200,y=300)

# l3 = Label(text="RESULT",font=("Bodoni Bd BT", 20) , bg="black",fg= "white")
# l3.place(x=900,y=260)

# f1 = Frame(win,height=400,width=500).place(x= 900,y=300)

# win.mainloop()




# ----------------------------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------------------------------------------


from tkinter import *
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import os
import shutil
import cv2
from skimage import io, img_as_ubyte, img_as_float, color
from skimage.restoration import denoise_nl_means
from skimage.filters import gaussian
from pywt import wavedec2, waverec2

def copy_image(input_path, output_path):
    try:
        if not os.path.exists(input_path):
            print("Input file does not exist.")
            return
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        shutil.copy2(input_path, output_path)
        print("Image copied successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def download():
    with open('basename.txt', 'r') as file:
        basename = file.read().strip()
    input_path = os.path.join("C:/Users/COMP/Desktop/IMG denoise/result", basename)
    output_path = os.path.join("C:/Users/COMP/Downloads", basename)
    copy_image(input_path, output_path)

def denoise_image(filepath):
    img = io.imread(filepath)
    
    img_float32 = cv2.resize(img_as_float(img), (350, 350))
    img_uint8 = img_as_ubyte(img_float32)
    
    if len(img_uint8.shape) == 3 and img_uint8.shape[2] == 3:
        R_channel, G_channel, B_channel = cv2.split(img_uint8)
        denoise_nl_means_R = denoise_nl_means(R_channel, h=0.1, sigma=0.02, patch_size=5, patch_distance=6)
        denoise_nl_means_G = denoise_nl_means(G_channel, h=0.1, sigma=0.02, patch_size=5, patch_distance=6)
        denoise_nl_means_B = denoise_nl_means(B_channel, h=0.1, sigma=0.02, patch_size=5, patch_distance=6)
        denoised_color_img_uint8 = cv2.merge([denoise_nl_means_R, denoise_nl_means_G, denoise_nl_means_B])
        denoised_color_img_uint8 = img_as_ubyte(denoised_color_img_uint8)
        cv2.imwrite(filepath, cv2.cvtColor(denoised_color_img_uint8, cv2.COLOR_BGR2RGB))
    else:
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

        gray_img_float32_resized = cv2.resize(img_as_float(color.rgb2gray(img_uint8)), (320, 480))
        denoise_gaussian_gray = denoise_gaussian(gray_img_float32_resized)
        denoise_cv2_gaussian_gray = denoise_cv2_gaussian(gray_img_float32_resized)
        denoise_wavelet_gray = denoise_wavelet(gray_img_float32_resized)
        ensemble_gray = (denoise_gaussian_gray + denoise_cv2_gaussian_gray + denoise_wavelet_gray) / 3
        ensemble_gray_uint8 = img_as_ubyte(ensemble_gray)
        cv2.imwrite(filepath, ensemble_gray_uint8)

def show_output(filepath):
    original_image = Image.open(filepath)
    resized_image = original_image.resize((500, 400), Image.LANCZOS)
    img1 = ImageTk.PhotoImage(resized_image)
    label1img = Label(canvas, image=img1, bg='white')
    label1img.image = img1
    label1img.place(x=900, y=300)

    downloadbtn = Button(canvas, text="Download", font=",20", bg="white", fg="black", command=download)
    downloadbtn.place(x=750, y=700)

def denoise():
    loader.start()
    filepath = "C:/Users/COMP/Desktop/IMG denoise/result"
    with open('basename.txt', 'r') as file:
        basename = file.read().strip()
    filepath = os.path.join(filepath, basename)
    
    def process_denoise():
        denoise_image(filepath)
        loader.stop()
        show_output(filepath)
    
    # Simulate a loading delay before starting the denoising process
    canvas.after(2000, process_denoise)  # Delay in milliseconds

def importimg():
    file_path = filedialog.askopenfilename(title="Select Input Image File", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;")])
    if file_path:
        basename = os.path.basename(file_path)
        with open('basename.txt', 'w') as basefile:
            basefile.write(basename)
        
        copy_image(file_path, os.path.join("C:/Users/COMP/Desktop/IMG denoise/userdata", basename))
        copy_image(file_path, os.path.join("C:/Users/COMP/Desktop/IMG denoise/result", basename))

        denoisbtn = Button(canvas, text="Denoise", font=",20", bg="white", fg="black", command=denoise)
        denoisbtn.place(x=750, y=400)
        
        original_image = Image.open(file_path)
        resized_image = original_image.resize((500, 400), Image.LANCZOS)
        img1 = ImageTk.PhotoImage(resized_image)
        label1img = Label(canvas, image=img1, bg='white')
        label1img.image = img1
        label1img.place(x=200, y=300)

class Loader:
    def __init__(self, parent):
        self.progress = ttk.Progressbar(parent, mode='indeterminate')
    
    def start(self):
        self.progress.place(x=750, y=500)  # Adjust the x and y coordinates as needed
        self.progress.start()
    
    def stop(self):
        self.progress.stop()
        self.progress.place_forget()

win = Tk()
win.state("zoomed")
win.title("IMAGE DENOISING")

# Add a background image
# bg_image_path = r"C:\Users\COMP\Desktop\Final Project\wizard-sm.jpg"  # Use raw string by adding 'r' before the string
bg_image_path = os.path.join(base_dir, 'wizard-sm.jpg')
bg_image = Image.open(bg_image_path)
bg_image = bg_image.resize((win.winfo_screenwidth(), win.winfo_screenheight()), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = Canvas(win, width=win.winfo_screenwidth(), height=win.winfo_screenheight())
canvas.create_image(0, 0, anchor=NW, image=bg_photo)
canvas.pack(fill=BOTH, expand=True)

# Widgets
l1 = Label(canvas, text="IMAGE DENOISING", font=("Bernard MT Condensed", 20), bg="black", fg="white")
l1.place(x=690, y=30)

l4 = Label(canvas, text="→ REMOVE THE NOISE FROM IMAGE IN ONE CLICK", font=("Engravers MT", 20), bg="black", fg="white")
l4.place(x=365, y=125)

btn = Button(canvas, text="IMPORT IMAGE", font=",19", bg="LIGHTGREEN", fg="black", command=importimg)
btn.place(x=720, y=70)

l2 = Label(canvas, text="INPUT IMAGE", font=("Bodoni Bd BT", 20), bg="black", fg="white")
l2.place(x=200, y=260)

f1 = Frame(canvas, height=400, width=500, bg='white')
f1.place(x=200, y=300)

l3 = Label(canvas, text="RESULT", font=("Bodoni Bd BT", 20), bg="black", fg="white")
l3.place(x=900, y=260)

f2 = Frame(canvas, height=400, width=500, bg='white')
f2.place(x=900, y=300)

loader = Loader(canvas)

win.mainloop()




