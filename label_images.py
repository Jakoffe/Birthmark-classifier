import sys
import json
import shutil
import os


path_of_descriptions = "/Users/jakof/Desktop/BirthmarkGPU/Data/Descriptions/"
path_of_images = "/Users/jakof/Desktop/BirthmarkGPU/Data/Images/"
image_file_extension = ".jpeg"
image_destination_path = "/Users/jakof/Desktop/BirthmarkGPU/Data/Labeled/"

#Counters
key_Error_Counter = 0
benign_counter = 0
malignant_counter = 0

def main(image_path, description_path, image_destination_path):
	prework(image_destination_path)

	for file in os.listdir(description_path):
		load_json(description_path + file)


def load_json(filepath):
	with open(filepath) as file:
		file_name = os.path.basename(filepath)
		data = json.load(file)
		try: #The "benign_malignant" field is not always present.
			benign_malignant = data["meta"]["clinical"]["benign_malignant"]
			label(path_of_images + file_name + image_file_extension, benign_malignant)
		except KeyError:
			#If KeyError do nothing but count the number of KeyErrors.
			global key_Error_Counter
			key_Error_Counter += 1

def label(filepath, benign_malignant):
	if os.path.isfile(filepath):
		global benign_counter
		global malignant_counter
		if benign_malignant == "benign":
			shutil.copy(filepath, image_destination_path + "Benign/" + benign_malignant + str(benign_counter) + image_file_extension)
			benign_counter += 1
		elif benign_malignant == "malignant":
			shutil.copy(filepath, image_destination_path + "Malignant/" + benign_malignant + str(malignant_counter) + image_file_extension)
			malignant_counter += 1

def prework(destination_path):
	if not os.path.exists(destination_path):
	    os.makedirs(destination_path)
	if not os.path.exists(destination_path + "Benign"):
	    os.makedirs(destination_path + "Benign")
	if not os.path.exists(destination_path + "Malignant"):
	    os.makedirs(destination_path + "Malignant")


main(path_of_images, path_of_descriptions, image_destination_path)
print("Number of errors: ", key_Error_Counter)
