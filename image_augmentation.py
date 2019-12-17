from PIL import Image
from PIL import ImageOps
import os
import sys

def rotate_img(img_path, rotation = 0):
    global image_counter
    global image_folder_path

    img = Image.open(img_path)
    if rotation == 0:
        #Vertically
        img = ImageOps.mirror(img)
        img.save(image_folder_path + vertically_destination_folder + "malignant" + str(images + image_counter) + ".jpeg")
    elif rotation == 1:
    	#Horizontally
    	img = ImageOps.flip(img)
    	img.save(image_folder_path + horizontally_destination_folder + "malignant" + str(images + image_counter) + ".jpeg")
    else:
    	print("Rotation error.. Needs to be set to 0 or 1")
    image_counter += 1

def loadImages(filepath):
    global rotation
    prework(filepath)
    for file in os.listdir(filepath):
        if file.endswith('.jpeg'):
            rotate_img(filepath + file, rotation)

def prework(filepath):
    global vertically_destination_folder
    global horizontally_destination_folder
    global images

    if not os.path.exists(filepath + vertically_destination_folder):
        os.makedirs(filepath + vertically_destination_folder)
    if not os.path.exists(filepath + horizontally_destination_folder):
        os.makedirs(filepath + horizontally_destination_folder)

image_folder_path = sys.argv[1] #Image folder path
vertically_destination_folder = "Modified/Vertically/"
horizontally_destination_folder = "Modified/Horizontally/"
rotation = 1 #Rotate vertically = 0, horizontally = 1.
image_counter = 1
images = 4563
loadImages(image_folder_path)
